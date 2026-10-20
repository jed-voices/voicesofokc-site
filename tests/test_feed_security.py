"""Offline regression tests: fixture feed only, temporary output, no network."""
import ast
import contextlib
import html
import io
import json
import os
from pathlib import Path
import runpy
import socket
import tempfile
import types
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'scripts/update_podbean_data.py'
START = '<!-- ARCHIVE_STRUCTURED_DATA_START -->'
END = '<!-- ARCHIVE_STRUCTURED_DATA_END -->'


def helpers():
    # Load definitions without running the publisher or its module-level mkdir.
    tree = ast.parse(SOURCE.read_text())
    tree.body = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef, ast.Assign))
                 and not (isinstance(n, ast.Import) and any(a.name == 'feedparser' for a in n.names))]
    # Stop before publication's assignments (which depend on the fetched feed).
    tree.body = tree.body[:next(i for i, n in enumerate(tree.body) if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'feed' for t in n.targets))]
    ns = {}
    exec(compile(tree, str(SOURCE), 'exec'), ns)
    return ns


class FeedSecurity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.h = helpers()

    def test_plain_text_and_formatting(self):
        self.assertEqual(self.h['strip_html']('<p>Hope &amp; joy</p><p>Visit <a href="https://example.test">us</a>.</p>'), 'Hope & joy Visit us .')
        self.assertEqual(self.h['strip_html']('<script>bad()</script><style>bad</style>Hello<br>world'), 'Hello world')
        self.assertEqual(self.h['strip_html']('2 &lt; 3 &amp; 4 &gt; 1'), '2 < 3 & 4 > 1')
        self.assertEqual(self.h['strip_html']('&amp;lt;img src=x&amp;gt;'), '&lt;img src=x&gt;')

    def test_json_ld_round_trip_and_no_html_delimiters(self):
        title = END + '<img src=x onerror=bad()> & </script> \\1 \\u003c café'
        markup = self.h['structured_data_markup']({'name': title})
        body = markup.split('>', 1)[1].rsplit('</script>', 1)[0]
        self.assertFalse(any(c in body for c in '<>&'))
        self.assertEqual(json.loads(body)['name'], title)

    def test_marker_inside_old_script_is_not_boundary(self):
        old = START + '\n<script type="application/ld+json">' + json.dumps({'name': END + '<img src=x>'}) + '</script>\n' + END
        result = self.h['replace_marker_block'](old, START, END, '<script type="application/ld+json">{"safe":true}</script>')
        self.assertNotIn('<img', result)
        self.assertEqual(result.count(END), 1)

    def test_ambiguous_missing_reversed_markers_fail_closed(self):
        for document in (START + END + END, START, END + START):
            with self.subTest(document=document), self.assertRaises(SystemExit):
                self.h['replace_marker_block'](document, START, END, 'safe')

    def test_literal_backslashes_survive_replacement(self):
        content = r'{"title":"\\1 \\g<0> \\u003c"}'
        self.assertIn(content, self.h['replace_marker_block'](START + END, START, END, content))

    def test_full_publisher_two_runs_offline(self):
        title = 'Test ' + END + '<img src=x onerror=bad()> & \\1 café'
        descriptions = [html.escape('<img src=x onerror=bad()>'), html.escape(html.escape('<svg onload=bad()>')), '<p>Normal <strong>show notes</strong> &amp; links</p>']
        entries = [dict(title=title if i == 0 else 'Normal episode '+str(i), summary=s, link='https://example.test/'+str(i), enclosures=[{'href':'https://example.test/audio.mp3'}]) for i, s in enumerate(descriptions)]
        fake = types.ModuleType('feedparser')
        fake.parse = lambda _: types.SimpleNamespace(bozo=False, entries=entries, feed={})
        with tempfile.TemporaryDirectory() as tmp:
            cwd = os.getcwd()
            try:
                os.chdir(tmp)
                Path('episodes').mkdir()
                Path('episodes/index.html').write_text((ROOT / 'episodes/index.html').read_text())
                with patch.dict(os.environ, {'PODBEAN_FEED_URL':'fixture-only','YOUTUBE_CHANNEL_ID':'','YOUTUBE_API_KEY':''}, clear=True), patch.dict('sys.modules', {'feedparser':fake}), patch('urllib.request.urlopen', side_effect=AssertionError('Network forbidden')), patch.object(socket.socket, 'connect', side_effect=AssertionError('Network forbidden')), contextlib.redirect_stdout(io.StringIO()):
                    runpy.run_path(str(SOURCE))
                    first = Path('episodes/index.html').read_text()
                    runpy.run_path(str(SOURCE))
                archive = Path('episodes/index.html').read_text()
                self.assertEqual(first, archive)
                self.assertEqual(archive.count(START), 1)
                self.assertEqual(archive.count(END), 1)
                self.assertNotIn('<img src=x', archive)
                self.assertNotIn('<svg onload', archive)
                data = json.loads(Path('assets/data/episodes.json').read_text())['episodes']
                self.assertEqual(data[0]['title'], title)
                self.assertEqual(data[2]['summary'], 'Normal show notes & links')
                self.assertEqual(data[0]['audio_url'], 'https://example.test/audio.mp3')
                self.assertEqual(json.loads(Path('assets/data/latest-episode.json').read_text())['summary'], data[0]['summary'])
                page = Path(data[2]['site_path'], 'index.html').read_text()
                self.assertIn('<strong>show notes</strong>', page)
                self.assertIn('https://example.test/audio.mp3', page)
            finally:
                os.chdir(cwd)

if __name__ == '__main__':
    unittest.main()

import io
import os
import sys
import test
import traceback
import unittest

from plain_json_logging import PlainJsonLogging

class Test(unittest.TestCase):

    def setUp(self):
        self.stderr = io.StringIO()
        sys.stderr = self.stderr
        self.stdout = io.StringIO()
        sys.stdout = self.stdout

    def name(self):
        return traceback.extract_stack(None, 2)[0][2]

    def test_stderr(self):
        name = self.name()
        case = {
            'error': '::{0}::e::'.format(name),
            'warn': '::{0}::w::'.format(name),
            'info': '::{0}::i::'.format(name),
        }

        logger = PlainJsonLogging(file=sys.stderr)
        logger.error(case['error'])
        logger.warn(case['warn'])
        logger.info(case['info'])

        self.assertTrue(self.stderr.getvalue().find(case['error']) > -1)
        self.assertTrue(self.stderr.getvalue().find(case['warn']) > -1)
        self.assertTrue(self.stderr.getvalue().find(case['info']) > -1)

    def test_stdout(self):
        name = self.name()
        case = {
            'error': '::{0}::e::'.format(name),
            'warn': '::{0}::w::'.format(name),
            'info': '::{0}::i::'.format(name),
        }

        logger = PlainJsonLogging(file=sys.stdout)
        logger.error(case['error'])
        logger.warn(case['warn'])
        logger.info(case['info'])

        self.assertTrue(self.stdout.getvalue().find(case['error']) > -1)
        self.assertTrue(self.stdout.getvalue().find(case['warn']) > -1)
        self.assertTrue(self.stdout.getvalue().find(case['info']) > -1)

    def test_partial_args(self):
        name = self.name()

        logger = PlainJsonLogging(
          file=sys.stderr,
          timezone='America/Chicago',
          timedelta=+60,
          levelinfo='INFORMATION',
        )
        logger.info('::{0}::i::'.format(name))

        self.assertTrue(self.stderr.getvalue().find('INFORMATION') > -1)

    def test_continuity(self):
        name = self.name()
        label = 'CONTINUTITY'
        case = [
            '::{0}::{1}::000::'.format(name, label),
            '::{0}::{1}::001::'.format(name, label),
            '::{0}::{1}::002::'.format(name, label),
        ]

        logger = PlainJsonLogging(
          file=sys.stderr,
          levelinfo='CONTINUTITY'
        )
        logger.info(
          case[0]
        ).info(
          case[1]
        ).info(
          case[2]
        )

        self.assertTrue(self.stderr.getvalue().find(case[0]) > -1)
        self.assertTrue(self.stderr.getvalue().find(case[1]) > -1)
        self.assertTrue(self.stderr.getvalue().find(case[2]) > -1)

    def test_file(self):
        name = self.name()
        case = {
            'error': '::{0}::e::'.format(name),
            'warn': '::{0}::w::'.format(name),
            'info': '::{0}::i::'.format(name),
        }
        output = 'tests/out.file'

        with open(output, 'w+') as f:
            logger = PlainJsonLogging(file=f)
            logger.error(case['error'])
            logger.warn(case['warn'])
            logger.info(case['info'])

        with open(output) as f:
            content = f.read()
            self.assertTrue(content.find(case['error']) > -1)
            self.assertTrue(content.find(case['warn']) > -1)
            self.assertTrue(content.find(case['info']) > -1)
        os.remove(output)

    def test_example(self):
        name = self.name()
        case = {
            'info': {
                'msg': '::{0}::i::'.format(name),
                'ext': {
                    'infoData': 'this is a extra payload for info.',
                }
            },
            'warn': {
                'msg': '::{0}::w::'.format(name),
                'ext': {
                    'warnData': 'this is a extra payload for warn.',
                }
            },
            'error': {
                'msg': '::{0}::e::'.format(name),
                'ext': {
                    'errorData': 'this is a extra payload for error.'
                }
            },
        }
        output = 'tests/out.example'

        with open(output, 'w+') as f:
            logger = PlainJsonLogging(
              file=f,
              strftime='%Y-%m-%d %H:%M:%S.%f%z',
              timezone='Asia/Tokyo',
              timedelta=+540, # 9 hours
              timestampname='@timestamp',
              messagename='@message',
              levelname='level',
              levelinfo=0,
              levelwarn=1,
              levelerror=2,
              constextra={ 'name': 'Example' },
            )
            logger.info(case['info']['msg'], case['info']['ext'])
            logger.warn(case['warn']['msg'], case['warn']['ext'])
            logger.error(case['error']['msg'], case['error']['ext'])

        with open(output) as f:
            content = f.read()
            self.assertTrue(content.find('"level": 0') > -1)
            self.assertTrue(content.find('"level": 1') > -1)
            self.assertTrue(content.find('"level": 2') > -1)
            self.assertTrue(content.find('infoData') > -1)
            self.assertTrue(content.find('warnData') > -1)
            self.assertTrue(content.find('errorData') > -1)
            self.assertTrue(content.find('"name": "Example"') > -1)
            self.assertTrue(content.find(case['info']['ext']['infoData']) > -1)
            self.assertTrue(content.find(case['warn']['ext']['warnData']) > -1)
            self.assertTrue(content.find(case['error']['ext']['errorData']) > -1)

        os.remove(output)

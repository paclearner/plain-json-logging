import inspect
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
        logger = PlainJsonLogging(file=sys.stderr)
        case = {
            'error': name + '::e1::',
            'warn': name + '::w2::',
            'info': name + '::i3::',
        }
        logger.error(case['error'])
        logger.warn(case['warn'])
        logger.info(case['info'])
        self.assertTrue(self.stderr.getvalue().find(case['error']) > -1)
        self.assertTrue(self.stderr.getvalue().find(case['warn']) > -1)
        self.assertTrue(self.stderr.getvalue().find(case['info']) > -1)

    def test_stdout(self):
        name = self.name()
        logger = PlainJsonLogging(file=sys.stdout)
        case = {
            'error': name + '::e1::',
            'warn': name + '::w2::',
            'info': name + '::i3::',
        }
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
          timedelta=+60,
          inforname='INFORMATION'
        )
        logger.info(name + 'info')
        self.assertTrue(self.stderr.getvalue().find('INFORMATION') > -1)

    def test_file(self):
        name = self.name()
        output = 'tests/test.out'
        with open(output, 'w+') as f:
            logger = PlainJsonLogging(file=f)
            case = {
                'error': name + '::e1::',
                'warn': name + '::w2::',
                'info': name + '::i3::',
            }
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
        output = 'tests/test.example.out'
        with open(output, 'w+') as f:
            logger = PlainJsonLogging(
              file=f,
              strftime='%Y-%m-%d %H:%M:%S.%f%z',
              timedelta=+540, # 9 hours
              timestampname='@timestamp',
              levelname='level',
              messagename='@message',
            )
            logger.info(name + '::this is info::', { 'infoData': 'this is a extra payload for info.'})
            logger.warn(name + '::this is warn::', { 'warnData': 'this is a extra payload for warning.'})
            logger.error(name + '::this is error::', { 'errData': 'this is a extra payload for warning.'})
        with open(output) as f:
            content = f.read()
            self.assertTrue(content.find('this is a extra payload for info.') > -1)
            self.assertTrue(content.find('this is a extra payload for warning.') > -1)
            self.assertTrue(content.find('this is a extra payload for warning.') > -1)
        os.remove(output)

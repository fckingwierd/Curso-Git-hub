from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from asd import AssertionTests
from searchtests import SearchTests

assertion_test = TestLoader().loadTestsFromTestCase(AssertionTests)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assertion_test, search_test])

kwargs = {
    "output": "smoke-report"
}
runner = HTMLTestRunner(**kwargs)

runner.run(smoke_test)
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = 'What language did you first learn to speak? '
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']


    def test_store_single_response(self):
        """针对单个答案会被妥善地保存"""
        self.my_survey.store_response(self.responses[0])

        # 使用 assertEqual 替代 assertEquals
        self.assertEqual(['English'], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善的储存"""
        for response in self.responses:
            self.my_survey.store_response(response)

        # 使用 assertEqual 替代 assertEquals
        self.assertEqual(self.responses, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()

"""
注意"运行测试用例时，每完成一个单元测试，Python都打印一个宇符：测试通过时打印一个
句点；测试引发错误时打印一个E；测试导致断言失败时打印一个F。这就是你运行测战
用例时，在输出的第一行中看到的句点和字符数量各不相同的原因。如果测试用例包含很多单元测试，
需要运行很长时间，就可通过观察这些结果来获悉有多少个测试通过了
"""
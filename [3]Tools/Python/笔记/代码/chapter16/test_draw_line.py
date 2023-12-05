import unittest
import json
import os
from itertools import groupby
from btc_close_2017 import draw_line  # Import your draw_line function here
from btc_close_2017 import generate_html

class DrawLineTestCase(unittest.TestCase):
    """用于绘制曲线类的测试"""

    def setUp(self):
        """初始化样例数据"""
        filename = 'btc_close_2017.json'
        with open(filename) as f:
            btc_data = json.load(f)

        # 存储每一天的信息
        self.dates, self.months, self.weeks, self.weekdays, self.close = [], [], [], [], []
        self.dates = [btc_dict['date'] for btc_dict in btc_data]
        self.months = [int(btc_dict['month']) for btc_dict in btc_data]
        self.weeks = [int(btc_dict['week']) for btc_dict in btc_data]
        self.weekdays = [btc_dict['weekday'] for btc_dict in btc_data]
        self.close = [int(float(btc_dict['close'])) for btc_dict in btc_data]

    def get_value_string_list(self, line_chart):
        # 获取原始数据系列
        raw_series = line_chart.raw_series

        # 遍历每个数据系
        values_list = []
        title_string = ''
        for series_index in range(len(raw_series)):
            # 使用整数索引获取元组中的字典
            series_data = raw_series[series_index]
            # 获取数值列表
            values_list = list(series_data[0])
            # 获取标题字符串
            title_string = series_data[1]['title']
        return values_list, title_string

    def test_month_draw_line(self):
        """能够正确处理收盘价月日均值"""
        title = '收盘价月日均值（¥）'
        legend = '月日均值'
        idx_month = self.dates.index('2017-12-01')

        # 调用绘图函数
        line_chart_month = draw_line(
            self.months[:idx_month], self.close[:idx_month], title, legend)
        values_list, title_string = self.get_value_string_list(line_chart_month)

        # 断言标题是否设置正确
        self.assertEqual(line_chart_month.title, title)
        self.assertEqual(title_string, legend)

        # 断言 x 轴标签是否设置正确
        self.assertEqual(line_chart_month.x_labels, list(set(self.months[:idx_month])))

        # 断言数据点的数量是否正确
        expected_num_points = len(set(self.months[:idx_month]))
        self.assertEqual(len(values_list), expected_num_points)

        # 断言数据点的数值是否正确
        xy_map = []
        for x, y in groupby(sorted(zip(self.months[:idx_month], self.close[:idx_month])), key=lambda _: _[0]):
            y_list = [v for _, v in y]
            xy_map.append([x, sum(y_list) / len(y_list)])
        x_unique, y_mean = [*zip(*xy_map)]

        expected_points = [(x, y) for x, y in zip(x_unique, y_mean)]
        line_chart_month_points = [(x, y) for x, y in zip(set(self.months[:idx_month]), values_list)]
        self.assertEqual(line_chart_month_points, expected_points)

        # 检查生成的文件是否存在
        file_path = title + '.svg'
        self.assertTrue(os.path.exists(file_path))

    def test_week_draw_line(self):
        """能够正确处理收盘价周日均值"""
        title = '收盘价周日均值（¥）'
        legend = '周日均值'
        idx_week = self.dates.index('2017-12-11')

        # 调用绘图函数
        line_chart_week = draw_line(
            self.weeks[1:idx_week], self.close[1:idx_week], title, legend)

        # 获取原始数据系列
        values_list, title_string = self.get_value_string_list(line_chart_week)

        # 断言标题是否设置正确
        self.assertEqual(line_chart_week.title, title)
        self.assertEqual(title_string, legend)

        # 断言 x 轴标签是否设置正确
        self.assertEqual(line_chart_week.x_labels, list(set(self.weeks[1:idx_week])))

        # 断言数据点的数量是否正确
        expected_num_points = len(set(self.weeks[1:idx_week]))
        self.assertEqual(len(values_list), expected_num_points)

        # 断言数据点的数值是否正确
        xy_map = []
        for x, y in groupby(sorted(zip(self.weeks[1:idx_week], self.close[1:idx_week])), key=lambda _: _[0]):
            y_list = [v for _, v in y]
            xy_map.append([x, sum(y_list) / len(y_list)])
        x_unique, y_mean = [*zip(*xy_map)]

        expected_points = [(x, y) for x, y in zip(x_unique, y_mean)]
        line_chart_month_points = [(x, y) for x, y in zip(set(self.weeks[1:idx_week]), values_list)]
        self.assertEqual(line_chart_month_points, expected_points)

        # 检查生成的文件是否存在
        file_path = title + '.svg'
        self.assertTrue(os.path.exists(file_path))

    def test_weekday_draw_line(self):
        """能够正确处理收盘价星期均值"""
        title = '收盘价星期均值（¥）'
        legend = '星期均值'
        idx_week = self.dates.index('2017-12-11')
        wd = ['Monday', 'Tuesday', 'Wednesday',
              'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekdays_int = [wd.index(w) + 1 for w in self.weekdays[1:idx_week]]

        # 调用绘图函数
        line_chart_weekday = draw_line(
            weekdays_int, self.close[1:idx_week], title, legend)
        line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        line_chart_weekday.render_to_file('收盘价星期均值（¥）.svg')

        # 获取原始数据系列
        values_list, title_string = self.get_value_string_list(line_chart_weekday)

        # 断言标题是否设置正确
        self.assertEqual(line_chart_weekday.title, title)
        self.assertEqual(title_string, legend)

        # 断言 x 轴标签是否设置正确
        self.assertEqual(line_chart_weekday.x_labels, ['周一', '周二', '周三', '周四', '周五', '周六', '周日'])

        # 断言数据点的数量是否正确
        expected_num_points = len(set(weekdays_int))
        self.assertEqual(len(values_list), expected_num_points)

        # 断言数据点的数值是否正确
        xy_map = []
        for x, y in groupby(sorted(zip(weekdays_int, self.close[1:idx_week])), key=lambda _: _[0]):
            y_list = [v for _, v in y]
            xy_map.append([x, sum(y_list) / len(y_list)])
        x_unique, y_mean = [*zip(*xy_map)]

        expected_points = [(x, y) for x, y in zip(x_unique, y_mean)]
        line_chart_month_points = [(x, y) for x, y in zip(set(weekdays_int), values_list)]
        self.assertEqual(line_chart_month_points, expected_points)

        # 检查生成的文件是否存在
        file_path = title + '.svg'
        self.assertTrue(os.path.exists(file_path))

    def test_generate_html(self):
        # 生成测试用例
        test_file_path = 'test_output.html'
        generate_html(test_file_path)

        # 读取生成的 HTML 文件内容
        with open(test_file_path, 'r', encoding='utf8') as test_file:
            generated_html = test_file.read()

        # 定义期望的 HTML 结构
        expected_html = '<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n'
        for svg in [
                '收盘价折线图（¥）.svg', '收盘价对数变换折线图（¥）.svg', '收盘价月日均值（¥）.svg',
                '收盘价周日均值（¥）.svg', '收盘价星期均值（¥）.svg'
        ]:
            expected_html += '    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg)
        expected_html += '</body></html>'

        # 断言实际生成的 HTML 与期望的 HTML 相等
        self.assertEqual(generated_html, expected_html)

        # 删除测试生成的 HTML 文件
        # 注意: 这里可能需要更好的处理方式，比如使用临时目录来保存测试文件
        # 以确保测试完成后可以清理测试文件
        import os
        os.remove(test_file_path)

if __name__ == '__main__':
    unittest.main()

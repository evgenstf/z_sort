'''

Types of charts:

- 'pie' -- Pie chart
    params:
        - 'labels'
        - 'ratio' (from 0 to 100, sum = 100)

- 'line' -- Linear chart
    params:
        - 'x-axis'
        - 'y-axis'
    optional:
        - 'color'
        - 'grid' (True or False, False default)

- 'scatter' -- Scatter chart
    params:
        - 'x-axis'
        - 'y-axis'
    optional:
        - 'color'
        - 'grid' (True or False, False default)

- 'bar' -- Bar chart
    params:
        - 'x-axis'
        - 'y-axis'
    optional:
        - 'color'
        - 'grid' (True or False, False default)

'''


import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline


class DrawChart:
    def __init__(self, data):
        self.chart_type = data['content']['type']
        if 'show_grid' in data['content']:
            self.show_grid = data['content']['show_grid']
        else:
            self.show_grid = False

        if self.chart_type == 'pie':
            self.pie_ratio = data['content']['ratio']
            self.labels = data['content']['labels']

        else:
            if 'color' in data['content']:
                self.plot_color = data['content']['color']
            else:
                self.plot_color = '#BF00B0'
            self.x_axis = data['content']['x-axis']
            self.y_axis = data['content']['y-axis']

        if 'line_smooth' in data['content'] and data['content']['line_smooth'] == True:
            self.line_smooth = True
        else:
            self.line_smooth = False

    def draw(self, path):
        plt.figure(figsize=(16, 12))
        plt.rcParams.update({'font.size': 30})

        if self.chart_type == 'pie':
            explode = list(map(lambda x: x / 8000, self.pie_ratio))
            plt.pie(self.pie_ratio, explode=explode, labels=self.labels, autopct='%1.1f%%')

        elif self.chart_type == 'scatter':
            plt.scatter(self.x_axis, self.y_axis, s = 350, c=self.plot_color)

        elif self.chart_type == 'line':
            if self.line_smooth == True:
                x_new = np.linspace(min(self.x_axis), max(self.x_axis), 300)
                spl = make_interp_spline(self.x_axis, self.y_axis, k=3)
                y_smooth = spl(x_new)
                plt.plot(x_new, y_smooth, color=self.plot_color, linewidth=8)
            else:
                plt.plot(self.x_axis, self.y_axis, color=self.plot_color, linewidth=8)
        elif self.chart_type == 'bar':
            plt.bar(self.x_axis, self.y_axis, color=self.plot_color)

        if self.show_grid == True:
            plt.grid()

        plt.savefig(path)
        plt.close()


class ChartSectionFactory:
    chart_id = 0

    @staticmethod
    def build_html(section, article_relative_path, static_resources_path):
        article_static_resources_path = static_resources_path + '/articles/' + article_relative_path
        if not os.path.exists(article_static_resources_path):
            os.makedirs(article_static_resources_path)

        chart_absolute_path = article_static_resources_path + '/' + "chart_" + str(ChartSectionFactory.chart_id) + ".svg"
        chart_relative_path = article_relative_path + '/' + "chart_" + str(ChartSectionFactory.chart_id) + ".svg"
        chart = DrawChart(section)
        chart.draw(chart_absolute_path)
        ChartSectionFactory.chart_id += 1

        return "<img src=\"{% static \"articles/" + chart_relative_path + "\" %}\" />"

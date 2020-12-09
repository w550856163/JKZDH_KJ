# -*- coding: utf-8 -*-
#@File ：excel_utils.py
#@Auth ： wwd
#@Time ： 2020/12/7 9:13 下午
import xlrd3
import os
class ExcelUtils:
    def __init__(self,excel_file_path,sheet_name):
        self.excel_file_path=excel_file_path
        self.sheet_name =sheet_name
        self.sheet = self.get_sheet()

    def get_sheet(self):
        ''' 根据文件路径及表格名称获取表格对象 '''
        work_book =xlrd3.open_workbook(self.excel_file_path)
        sheet=work_book.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        '''获取表格的行数'''
        row_count=self.sheet.nrows
        return row_count

    def get_column_count(self):
        '''获取表格的列数'''
        column_count =self.sheet.ncols
        return column_count


    def get_merge_cell_value(self,row_index,col_index):
        ''' 获取excel单元格的数据（包含合并单元格的数据）'''
        cell_value = None
        for (min_row, max_row, min_col, max_col) in self.sheet.merged_cells:
            if row_index >= min_row and row_index < max_row:
                if col_index >= min_col and col_index < max_col:
                    cell_value = self.sheet.cell_value(min_row, min_col)  # 合并单元格的值等于合并第一个单元格的值
                    break;
                else:
                    cell_value = self.sheet.cell_value(row_index, col_index)
            else:
                cell_value = self.sheet.cell_value(row_index, col_index)
        return cell_value

    def get_all_data(self):
        ''' 把excel数据转换成如下格式
        [{"字段名1":"字段值1","字段名2":"字段值2"...},{}]
        '''
        excel_list_data = []
        row_head = self.sheet.row_values(0)  # ==字典的key 首行的数据
        for row_num in range(1, self.get_row_count()):
            row_dict = {}
            for col_num in range(self.get_column_count()):
                row_dict[row_head[col_num]] = self.get_merge_cell_value(row_num, col_num) #获取一个单元格的数据
            excel_list_data.append(row_dict)
        return excel_list_data

if __name__=='__main__':
    file_path = os.path.join( os.path.dirname(__file__),'..','data','testcase_infos.xlsx')
    excelUtils = ExcelUtils(file_path,'Sheet1')
    for excel_row in excelUtils.get_all_data():
        print( excel_row )

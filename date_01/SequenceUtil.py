from date_01.log import logger


class SequenceUtil:

    @classmethod
    def list_common_transform_str(cls, data):
        """公共的将列表的值变为字符类型，使用join方法连接.

        :param data: 需要转换的序列数据.
        :return: str
        """
        list_data = []
        for i in data:
            list_data.append(str(i))
        return ''.join(list_data)

    @classmethod
    def list_common_transform_to_dict(cls, data) -> dict:
        """公共的list转换为dict方法.

        :param data: 需要转换的序列数据.
        :return: dict
        """
        dic_data = {}
        for i in range(0, len(data)):
            dic_data.update({str(i): data[i]})
        return dic_data

    @classmethod
    def transform_to_list(cls, sequence_data) -> list:
        """
        :param sequence_data: 需要转换的数据.
        :return: 返回list
        """

        if isinstance(sequence_data, list):
            return sequence_data

        # str转换为list
        if isinstance(sequence_data, str):
            return [i for i in sequence_data]

        # dict转换为list
        if isinstance(sequence_data, dict):
            return [value for _, value in sequence_data.items()]

        # tuple转换为list
        if isinstance(sequence_data, tuple):
            return [i for i in sequence_data]

        # set转换为list
        if isinstance(sequence_data, set):
            return [i for i in sequence_data]

    @classmethod
    def transform_to_str(cls, sequence_data) -> str:
        if isinstance(sequence_data, str):
            return sequence_data

        # list转换为str
        if isinstance(sequence_data, list):
            return SequenceUtil.list_common_transform_str(sequence_data)

        # dict转换为str
        if isinstance(sequence_data, dict):
            new_data = [str(value) for _, value in sequence_data.items()]
            return SequenceUtil.list_common_transform_str(new_data)

        # tuple转换为str
        if isinstance(sequence_data, tuple):
            new_data = SequenceUtil.transform_to_list(sequence_data)
            return SequenceUtil.list_common_transform_str(new_data)

        # set转换为str
        if isinstance(sequence_data, set):
            new_data = SequenceUtil.transform_to_list(sequence_data)
            return SequenceUtil.list_common_transform_str(new_data)

    @classmethod
    def transform_to_dict(cls, sequence_data) -> dict:
        if isinstance(sequence_data, dict):
            return sequence_data

        # list，tuple,set转换为dict
        if isinstance(sequence_data, set):
            data = SequenceUtil.transform_to_list(sequence_data)
            return SequenceUtil.list_common_transform_to_dict(data)
        else:
            return SequenceUtil.list_common_transform_to_dict(sequence_data)

    @classmethod
    def transform_to_tuple(cls, sequence_data) -> tuple:
        if isinstance(sequence_data, dict):
            return tuple(SequenceUtil.transform_to_list(sequence_data))
        else:
            return tuple(sequence_data)

    @classmethod
    def transform_to_set(cls, sequence_data) -> set:
        if isinstance(sequence_data, dict):
            data = SequenceUtil.transform_to_list(sequence_data)
            return set(data)
        else:
            return set(sequence_data)


s = SequenceUtil.transform_to_str({'name': 2, 'age': 1})

logger.info('执行成功')

print(s)

# 测试代码
# if __name__ == '__main__':
#     s = SequenceUtil.transform_to_str({'name': 2, 'age': '123'})
#     logget.info('执行成功')
#     print(s)

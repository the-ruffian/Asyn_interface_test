"""
 * @Description:请求封装
 * @CreatedBy:PyCharm
 * @Author: the-ruffian
 * @Date: 2021-09-09 21:12 
 * @LastEditTime: 2021-9-10 21:31:44
 * @LastEditors: the-ruffian
"""
import httpx


class Util:
    @staticmethod
    def post(**kwargs):
        return httpx.post(**kwargs)

    @staticmethod
    def get(**kwargs):
        return httpx.get(**kwargs)

    @staticmethod
    def put(**kwargs):
        return httpx.put(**kwargs)

    @staticmethod
    def delete(**kwargs):
        return httpx.delete(**kwargs)

    @staticmethod
    def options(**kwargs):
        return httpx.options(**kwargs)

    def main(self, method, **kwargs):
        if method == 'post':
            return self.post(**kwargs)
        if method == 'get':
            return self.get(**kwargs)
        if method == 'put':
            return self.put(**kwargs)
        if method == 'delete':
            return self.delete(**kwargs)
        if method == 'options':
            return self.options(**kwargs)

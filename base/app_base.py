from base.base import Base


class AppBase(Base):
    # 查找页面是否存在指定元素
    def app_base_element_is_exist(self, loc):
        try:
            # 1. 调用查找方法
            self.base_find(loc, timeout=3)
            # 2. 输出信息
            print('找到了元素: {}信息'.format(loc))
            # 3. 返回True
            return True
        except:
            # 1. 输出信息
            print('没有找到元素: {}信息'.format(loc))
            # 2. 返回False
            return False

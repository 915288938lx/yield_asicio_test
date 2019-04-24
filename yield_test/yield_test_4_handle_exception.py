class DemoException(Exception):
    def demo_finally(self):
        try:
            x = yield
        except DemoException:
            print('Exception handled, continuing...')
        else:
            print('coroutine received : ......')
        finally:
            print('coroutine ending')


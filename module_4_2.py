def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

# inner_function() функция не работает, потому что она находится в локальной области видимости, а не глобальной
test_function()

def fluar ():
    def fdalam():
        print('fdalam() dipanggil')
#perintah fungsi untuk fluar()
        print ('fluar() dipanggil')
    #memanggil fungsi fdalam()
    fdalam()
fluar()

def outer_function(siapa):
    def inner_function():
        print(f"hello,{siapa}")
    inner_function()
outer_function("albi ganteng")
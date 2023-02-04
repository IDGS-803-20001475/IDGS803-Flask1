from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/operasBas", methods=["GET","POST"])
def operasBas():
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        opc=request.form.get("opc")

        if opc == '1':
            return "La suma es: {}".format(str(int(num1)+int(num2)))
        elif opc == '2':
            return "La resta es: {}".format(str(int(num1)-int(num2)))
        elif opc == '3':
            return "La multiplicacion es: {}".format(str(int(num1)*int(num2)))
        elif opc == '4':
            return "La division es: {}".format(str(int(num1)/int(num2)))
    else:
        return '''
            <form action="/operasBas" method="POST">
            <label>N1: </label>
            <input type="text" name="num1"/></br></br>
            <label>N2: </label>
            <input type="text" name="num2"/></br></br>
            <input type="radio" value="1" name="opc"/>Suma
            <input type="radio" value="2" name="opc"/>Resta
            <input type="radio" value="3" name="opc"/>Multiplicacion
            <input type="radio" value="4" name="opc"/>Division</br></br>
            <input type="submit" value="operasBas"/>
            </form>

        '''

if __name__=="__main__":
    app.run(debug=True)
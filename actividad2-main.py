from flask import Flask, render_template
from flask import request

app=Flask(__name__)

class calculos():
    cantidadC = 0
    precioB = 12.000
    nombre = ""
    cantidadB = 0
    pagoCineco = False

    def validarC(self):
        cantidadMaximaB = self.cantidadC * 7
        print(cantidadMaximaB)
        if self.cantidadB <= cantidadMaximaB:
         return cantidadMaximaB
        else:
            return 0

    def realizarC(self):
        res = self.cantidadB * self.precioB
        if self.cantidadB > 5:
            res = res - (res * 0.15)
        elif self.cantidadB >= 3 and self.cantidadB <= 5:
            res = res - (res * 0.10)
        if self.pagoCineco == True:
            res = res - (res * 0.10)
        return res

        

@app.route("/index")
def index():

    return render_template("actividad2-index.html")

@app.route("/res", methods=["POST"])
def res():
        nombre = request.form.get("txtNombre")
        cantidadC = request.form.get("txtCantidad")
        cantidadB = request.form.get("txtCantidadB")
        pagoCineco = request.form.get("opc")
    
        obj = calculos()
        obj.nombre = nombre
        obj.cantidadC = int(cantidadC)
        obj.cantidadB = int(cantidadB)
        if pagoCineco == "1":
            obj.pagoCineco = True
        else:
            obj.pagoCineco = False
    
        maxPermitidos = obj.validarC()

        if maxPermitidos != 0:
            res = obj.realizarC()
            print(res)
            return render_template("actividad2-Resultado.html", nombre=nombre, permitidos=maxPermitidos, pedidos =cantidadB, total=res)    
        else:
            boletosPermitidos = int(cantidadC) * 7
            return '''
            <h3>La cantidad maxima de boletos por persona es 7</h3>

            '''
if __name__=="__main__":
    app.run(debug=True)
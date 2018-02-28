from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session

app = Flask(__name__)

app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/iniciarTest', methods=['POST'])
def inicio():
    if request.method == 'POST':
        session['desde'] = float(request.form['desde'])
        session['hasta'] = float(request.form['hasta'])
        session['H']=float(request.form['N'])
        if session['H'] == 2:
            h=(session['hasta']-session['desde'])/session['H']
            c11=session['desde']
            c12=h+c11
            c13=c12+h
            respuesta = make_response(render_template('N2.html', c11=c11, c12=c12, c13=c13, h=h))
        elif session['H'] == 3:
            h=(session['hasta']-session['desde'])/session['H']
            c11=session['desde']
            c12=h+c11
            c13=c12+h
            c14=session['hasta']
            respuesta = make_response(render_template('N3.html', c11=c11, c12=c12, c13=c13, c14=c14, h=h))
        elif session['H']==4:
            h = (session['hasta'] - session['desde']) / session['H']
            c11 = session['desde']
            c12 = h + c11
            c13 = c12 + h
            c14 = c13 + h
            c15 = session['hasta']
            respuesta = make_response(render_template('N4.html', c11=c11, c12=c12, c13=c13, c14=c14, c15=c15, h=h))
        elif session['H']==5:
            h = (session['hasta'] - session['desde']) / session['H']
            c11 = session['desde']
            c12 = h + c11
            c13 = c12 + h
            c14 = c13 + h
            c15 = c14 + h
            c16 = session['hasta']
            respuesta = make_response(render_template('N5.html', c11=c11, c12=c12, c13=c13, c14=c14, c15=c15, c16=c16, h=h))
        elif session['H']==6:
            h = (session['hasta'] - session['desde']) / session['H']
            c11 = session['desde']
            c12 = h + c11
            c13 = c12 + h
            c14 = c13 + h
            c15 = c14 + h
            c16 = c15 + h
            c17 = session['hasta']
            respuesta = make_response(render_template('N6.html', c11=c11, c12=c12, c13=c13, c14=c14, c15=c15, c16=c16, c17=c17, h=h))
        elif session['H']==7:
            h = (session['hasta'] - session['desde']) / session['H']
            c11 = session['desde']
            c12 = h + c11
            c13 = c12 + h
            c14 = c13 + h
            c15 = c14 + h
            c16 = c15 + h
            c17 = c16 + h
            c18 = session['hasta']
            respuesta = make_response(render_template('N7.html', c11=c11, c12=c12, c13=c13, c14=c14, c15=c15, c16=c16, c17=c17, c18=c18, h=h))
        elif session['H']==8:
            h = (session['hasta'] - session['desde']) / session['H']
            c11 = session['desde']
            c12 = h + c11
            c13 = c12 + h
            c14 = c13 + h
            c15 = c14 + h
            c16 = c15 + h
            c17 = c16 + h
            c18 = c17 + h
            c19 = session['hasta']
            respuesta = make_response(render_template('N8.html', c11=c11, c12=c12, c13=c13, c14=c14, c15=c15, c16=c16, c17=c17, c18=c18, c19=c19, h=h))
        return respuesta

@app.route('/N2', methods=['POST'])
def N2():
    valor21 = float(request.form['21'])
    valor22 = float(request.form['22'])
    valor23 = float(request.form['23'])
    operacion=request.form['operacion']
    if operacion == 'Trapecio':
        resultado=((session['hasta']-session['desde'])/session['H'])*(valor21+(valor22*2)+valor23*2)
    elif operacion == '1/3':
        resultado=(((session['hasta']-session['desde'])/session['H'])*(1/3))*(valor21+(valor22*4)+valor23)

    respuesta = make_response(render_template('Resultado.html', S=resultado))
    return respuesta


@app.route('/N3', methods=['POST'])
def N3():
    valor21 = float(request.form['21'])
    valor22 = float(request.form['22'])
    valor23 = float(request.form['23'])
    valor24 = float(request.form['24'])
    operacion=request.form['operacion']
    if operacion == 'Trapecio':
        resultado=((session['hasta']-session['desde'])/session['H'])*(0.5)*(valor21+(valor22*2)+(valor23*2)+valor24)
    elif operacion == '3/8':
        resultado=(((session['hasta']-session['desde'])/session['H'])*(3/8))*(valor21+(valor22*3)+(valor23*3)+valor24)

    respuesta = make_response(render_template('Resultado.html', S=resultado))
    return respuesta

@app.route('/N4', methods=['POST'])
def N4():
    valor21 = float(request.form['21'])
    valor22 = float(request.form['22'])
    valor23 = float(request.form['23'])
    valor24 = float(request.form['24'])
    valor25 = float(request.form['25'])
    operacion=request.form['operacion']
    if operacion == 'Trapecio':
        resultado=((session['hasta']-session['desde'])/session['H'])*(0.5)*(valor21+(valor22*2)+(valor23*2)+(valor24*2)+valor25)
    elif operacion == '1/3':
        resultado=(((session['hasta']-session['desde'])/session['H'])*(1/3))*(valor21+(valor23*4)+valor25)

    respuesta = make_response(render_template('Resultado.html', S=resultado))
    return respuesta

@app.route('/N5', methods=['POST'])
def N5():
    valor21 = float(request.form['21'])
    valor22 = float(request.form['22'])
    valor23 = float(request.form['23'])
    valor24 = float(request.form['24'])
    valor25 = float(request.form['25'])
    valor26 = float(request.form['26'])
    operacion=request.form['operacion']
    if operacion == 'Trapecio':
        resultado=(((session['hasta']-session['desde'])/session['H'])*0.5)*(valor21+(valor22*2)+(valor23*2)+(valor24*2)+(valor25*2)+valor26)
    elif operacion == '3/8':
        resultado=(((session['hasta']-session['desde'])/session['H'])*(3/8))*(valor21+(valor22*3)+(valor23*3)+valor24)+(((session['hasta'] - session['desde']) / session['H']) * (1/3)) * (valor24 + (valor25 * 4) +valor26)

    respuesta = make_response(render_template('Resultado.html', S=resultado))
    return respuesta

@app.route('/N6', methods=['POST'])
def N6():
    valor21 = float(request.form['21'])
    valor22 = float(request.form['22'])
    valor23 = float(request.form['23'])
    valor24 = float(request.form['24'])
    valor25 = float(request.form['25'])
    valor26 = float(request.form['26'])
    valor27 = float(request.form['27'])
    operacion=request.form['operacion']
    if operacion == 'Trapecio':
        resultado=((session['hasta']-session['desde'])/session['H'])*(0.5)*(valor21+(valor22*2)+(valor23*2)+(valor24*2)+(valor25*2)+(valor26*2)+valor27)
    elif operacion == '1/3':
        resultado=(((session['hasta']-session['desde'])/2)*(1/3))*(valor21+(valor24*4)+valor27)
    respuesta = make_response(render_template('Resultado.html', S=resultado))
    return respuesta

@app.route('/N7', methods=['POST'])
def N7():
    valor21 = float(request.form['21'])
    valor22 = float(request.form['22'])
    valor23 = float(request.form['23'])
    valor24 = float(request.form['24'])
    valor25 = float(request.form['25'])
    valor26 = float(request.form['26'])
    valor27 = float(request.form['27'])
    valor28 = float(request.form['28'])
    operacion = request.form['operacion']
    if operacion == 'Trapecio':
        resultado = (((session['hasta'] - session['desde']) / session['H']) * 0.5) * (
        valor21 + (valor22 * 2) + (valor23 * 2) + (valor24 * 2) + (valor25 * 2) + (valor26*2) + (valor27*2) + valor28)
    elif operacion == '3/8':
        resultado = (((session['hasta'] - session['desde']) / session['H']) * (3 / 8)) * (
        valor21 + (valor22 * 3) + (valor23 * 3) + (valor24 * 3) + (valor25 * 3) + (valor26*3) + (valor27*3) + valor28)

    respuesta = make_response(render_template('Resultado.html', S=resultado))
    return respuesta

@app.route('/N8', methods=['POST'])
def N8():
    valor21 = float(request.form['21'])
    valor22 = float(request.form['22'])
    valor23 = float(request.form['23'])
    valor24 = float(request.form['24'])
    valor25 = float(request.form['25'])
    valor26 = float(request.form['26'])
    valor27 = float(request.form['27'])
    valor28 = float(request.form['28'])
    valor29 = float(request.form['29'])
    operacion = request.form['operacion']
    if operacion == 'Trapecio':
        resultado = (((session['hasta'] - session['desde']) / session['H']) * 0.5) * (
        valor21 + (valor22 * 2) + (valor23 * 2) + (valor24 * 2) + (valor25 * 2) + (valor26*2) + (valor27*2) + (valor28*2) + valor29)
    elif operacion == '1/3':
        resultado = (((session['hasta'] - session['desde']) / 2) * (1/3)) * (valor21 + (valor25 * 4) + valor29)

    respuesta = make_response(render_template('Resultado.html', S=resultado))
    return respuesta

@app.route('/Inicio', methods=['POST'])
def inicioo():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)

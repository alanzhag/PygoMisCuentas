# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 18:57:12 2017

@author: User2
"""
#(Campo,Tipo de Dato,Longitud,Posicion,Observaciones)
metaFormato = (
    ("Campo","Tipo de Dato","Longitud","Posicion","Observaciones")
)

formatoCabe = (
    ("Codigo Registro","Numerico",1,"1-1","Valor fijo 0 (cero)."),
    ("Codigo Banelco","Numerico",3,"2-4","Valor fijo 400"),
    ("Codigo Empresa","Numerico",4,"5-8","Valor fijo 0000"),
    ("Fecha de archivo","Numerico",8,"9-16","Fecha de generación de archivo AAAAMMDD"),
    ("Filler","Alfanumerico",264,"17-280","Completar con 0 (ceros).")
)

formatoDeta = (
    ("Codigo Registro","Numerico",1,"1-1","Fijo 5 (cinco)."),
    ("Nro de Referencia o Codigo de Pago Electronico","Numerico",19,"2-20","21-40",
    """Debe completarse de la siguiente manera:
    -Las primeras 15 posiciones se
    completan con datos de la factura
    -La posición 16 para identificar el
    concepto a facturar (si no se va a
    utilizar, completar con cero)
    -Los cuatro dígitos restantes para
    identificar el mes y el año de
    facturación con el formato MMAA."""),
    ("Codigo moneda","Numerico",1,"41-41","Fijo: 0 (cero)."),
    ("Fecha 1º vencimiento","Numerico",8,"42-49","AAAAMMDD"),
    ("Importe 1º vencimiento","Decimal",11,"50-60","Importe de 1º vencimiento."),
    ("Fecha 2º vencimiento","Numerico",8,"61-68","""AAAAMMDD. Si se usa, debe ser mayor al
    campo “Fecha 1º vencimiento”. Si no usa
    segundo vencimiento, completar el mismo
    valor informado para 'Fecha 1º vencimiento'"""),
    ("Importe 2º vencimiento","Decimal",11,"69-79","""Si se usa, no puede ser menor al campo
    'Importe 1º vencimiento'. Si no usa segundo
    vencimiento, completar con el mismo valor
    informado para Importe 1º vencimiento"""),
    ("Fecha 3º vencimiento","Numerico",8,"80-87","""AAAAMMDD. Si se usa, debe ser mayor al
    campo “Fecha 2º vencimiento”. Si no usa
    segundo vencimiento, completar el mismo
    valor informado para 'Fecha 2º vencimiento'"""),
    ("Importe 3º vencimiento","Decimal",11,"88-98","""Si se usa, no puede ser menor al campo
    'Importe 2º vencimiento'. Si no usa tercer
    vencimiento, completar con el mismo valor
    informado para Importe 2º vencimiento """),
    ("Filler 1","Numerico",19,"99-117","Completar con ceros"),
    ("Nro. Referencia Ant.","Alfanumerico",19,"118-136"," Repetir el valor informado en el campo 'Nro. Referencia'"),
    ("Mensaje Ticket","Alfanumerico",40,"137-176","""Datos a informar en el ticket de pago. Utilizar
    de la siguiente manera:
    - Utilizar las primeras 15 posiciones
    para informar el Ente al cual se está
    efectuando el pago, abreviando el
    nombre de modo que el pagador
    pueda identificar inequívocamente
    el Ente.
    - Utilizar las 25 posiciones restantes
    para información secundaria, como
    el concepto que se esta pagando y /
    o el período.
    Completar solo con letras mayúsculas (sin
    acentos, ni enie) y números. No admite
    caracteres especiales (puntos, comas,
    paréntesis, etc.). """),
    ("Mensaje Pantalla","Alfanumerico",15,"177-191","""Datos a informar en la pantalla de selección
    de la factura a pagar. Utilizar las primeras 15
    posiciones del campo “Mensaje en Ticket”
    para informar el Ente al cual se está
    efectuando el pago, abreviando el nombre de
    modo que el pagador pueda identificar
    inequívocamente el Ente.
    Completar solo con letras mayúsculas (sin
    acentos, ni “ñ”) y números. No admite
    caracteres especiales (puntos, comas,
    paréntesis, etc.). 
    """),
    ("Codigo de barras","Alfanumerico",60,"192-251","Completar con espacios."),
    ("Filler 2","Alfanumerico",29,"252-280","Completar con ceros.")
)

formatoPie = (
    ("Codigo Registro","Numerico",1,"1-1","Valor fijo 9 (nueve)."),
    ("Codigo Banelco","Numerico",3,"2-4","Valor fijo 400"),
    ("Codigo Empresa","Numerico",4,"5-8","Valor fijo 0000"),
    ("Fecha de archivo","Numerico",8,"9-16","Fecha de generacion de archivo AAAAMMDD."),
    ("Cantidad de registros","Numerico",7,"17-23","Cantidad de registros de detalle informados. Es la cantidad de renglones que tiene el detalle"),
    ("Filler 1","Alfanumerico",7,"24-30","Completar con 0 (ceros)."),
    ("Total importe","Decimal",11,"31-41","""Suma de los importes informados en el
    campo “Importe primer vencimiento” de
    cada registro incluido en detalle.
    Formato: 9 enteros y 2 decimales, sin
    separadores. """),
    ("Filler 2","Alfanumerico",239,"42-280","Completar con 0")
)

formatoTotales = (280,280,280)



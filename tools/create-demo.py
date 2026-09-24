import json,pathlib
root=pathlib.Path(__file__).resolve().parents[1]/'content'
def mc(id,topic,d,q,opts,answer,exp,hint=''):
 return dict(id=id,topic=topic,type='multiple-choice',difficulty=d,question=q,options=opts,answer=answer,explanation=exp,hint=hint,tags=[topic])
def tf(id,topic,d,q,answer,exp):
 return dict(id=id,topic=topic,type='true-false',difficulty=d,question=q,options=['Verdadero','Falso'],answer='Verdadero' if answer else 'Falso',explanation=exp,tags=[topic])
def num(id,topic,d,q,answer,exp,tol=0):
 return dict(id=id,topic=topic,type='numeric',difficulty=d,question=q,answer=answer,tolerance=tol,explanation=exp,tags=[topic])
def exact(id,topic,d,kind,q,accepted,exp,code=None,seconds=None):
 x=dict(id=id,topic=topic,type=kind,difficulty=d,question=q,answer=accepted[0],rubric={'mode':'exact','accepted':accepted},explanation=exp,tags=[topic]);
 if code:x['code']=code
 if seconds:x['seconds']=seconds
 return x
def keys(id,topic,d,kind,q,groups,answer,exp):
 return dict(id=id,topic=topic,type=kind,difficulty=d,question=q,answer=answer,rubric={'mode':'keywords','required':groups},explanation=exp,tags=[topic])
def selfcheck(id,topic,d,q,answer,exp):
 return dict(id=id,topic=topic,type='written',difficulty=d,question=q,answer=answer,rubric={'mode':'self-check'},explanation=exp,tags=[topic])
units=[
('calculo','calculo-demo','Fundamentos del cambio','Aritmética y primeras ideas de funciones, solo para demostrar el motor. Los contenidos reales se incorporan después.',[
mc('c-01','funciones',1,'Si f(x) = 2x + 3, ¿cuánto vale f(2)?',['5','7','9','11'],'7','Sustituye x por 2: 2·2 + 3 = 7.'),
num('c-02','funciones',1,'Si f(x) = x², calcula f(3).',9,'Sustituye 3 en x²: 3² = 9.'),
mc('c-03','funciones',2,'La función f(x) = x + 4 tiene f(0) igual a...',['0','1','4','−4'],'4','El valor de f(0) se obtiene sustituyendo x por 0.'),
num('c-04','funciones',2,'Si f(x) = 3x − 2 y f(x) = 10, ¿cuánto vale x?',4,'3x − 2 = 10 ⇒ 3x = 12 ⇒ x = 4.'),
exact('c-05','funciones',2,'short','Para f(x)=x+1, escribe el valor de f(−1).',['0'],'−1 + 1 = 0.'),
tf('c-06','ecuaciones',1,'Sumar el mismo número en ambos lados de una igualdad conserva la igualdad.',True,'La operación equivalente se realiza en ambos lados.'),
num('c-07','ecuaciones',1,'Resuelve 2x + 6 = 14. Escribe x.',4,'Resta 6 a ambos lados y divide 8 entre 2.'),
mc('c-08','ecuaciones',2,'¿Cuál es la solución de 5x = 20?',['2','4','5','10'],'4','Divide ambos miembros entre 5.'),
num('c-09','ecuaciones',2,'Resuelve 3(x − 1) = 12. Escribe x.',5,'Divide entre 3: x − 1 = 4; suma 1.'),
exact('c-10','ecuaciones',2,'puzzle','El sello exige la solución entera de x + 7 = 12. ¿Qué número introduces?',['5'],'Restar 7 a 12 da 5.')]),
('fisica','fisica-demo','Movimiento y medidas','Problemas introductorios con unidades. Esta selección es DEMO y no representa el programa oficial.',[
num('f-01','cinematica',1,'Un objeto recorre 20 m en 4 s a velocidad constante. ¿Cuál es su rapidez en m/s?',5,'Rapidez = distancia/tiempo = 20/4 = 5 m/s.'),
mc('f-02','cinematica',1,'¿Cuál unidad corresponde a rapidez?',['m','m/s','s','kg'],'m/s','Rapidez es distancia dividida por tiempo.'),
num('f-03','cinematica',2,'A 3 m/s durante 5 s, ¿qué distancia se recorre en metros?',15,'d = v·t = 3·5 = 15 m.'),
tf('f-04','cinematica',2,'Un objeto puede tener rapidez constante y cambiar de dirección.',True,'La rapidez es escalar; la velocidad vectorial puede cambiar si cambia la dirección.'),
exact('f-05','cinematica',2,'short','Escribe la fórmula de rapidez media como razón usando d y t (sin espacios).',['d/t','d÷t'],'Rapidez media = distancia recorrida dividida por tiempo transcurrido.'),
num('f-06','unidades',1,'¿Cuántos centímetros hay en 2 metros?',200,'1 m = 100 cm, entonces 2 m = 200 cm.'),
mc('f-07','unidades',1,'¿Cuál magnitud se mide en segundos?',['Masa','Tiempo','Longitud','Temperatura'],'Tiempo','El segundo es una unidad de tiempo en el SI.'),
num('f-08','unidades',2,'Convierte 1,5 km a metros.',1500,'Multiplica 1,5 por 1000: 1500 m.'),
exact('f-09','unidades',2,'timed','Reto rápido: ¿cuántos segundos hay en 2 minutos?',['120'],'1 min = 60 s; 2 min = 120 s.',seconds=40),
exact('f-10','unidades',2,'puzzle','Una puerta muestra 300 cm. Escribe esa longitud en metros.',['3','3,0','3.0'],'Divide 300 entre 100: 3 metros.')]),
('programacion','programacion-demo','Algoritmos de la forja','Condicionales y bucles en pseudocódigo de demostración. No se ejecuta código ingresado.',[
mc('p-01','condicionales',1,'Si edad = 18 y la condición es edad >= 18, ¿qué rama se ejecuta?',['Si','SiNo','Ninguna'],'Si','18 satisface la comparación >= 18.'),
tf('p-02','condicionales',1,'En una condición, 7 > 9 resulta verdadero.',False,'7 es menor que 9.'),
exact('p-03','condicionales',2,'predict-code','¿Qué se escribe al ejecutar este pseudocódigo?',['A'], 'La condición 4 mod 2 = 0 es verdadera.',code='n <- 4\nSi n MOD 2 = 0 Entonces\n  Escribir "A"\nSiNo\n  Escribir "B"\nFinSi'),
exact('p-04','condicionales',2,'complete-code','Completa la palabra faltante para cerrar el condicional.',['FinSi'],'PSeInt cierra un condicional Si con FinSi.',code='Si x > 0 Entonces\n  Escribir x\n_____'),
keys('p-05','condicionales',2,'debug-code','Encuentra el error: Si edad > 18 Entonces ... FinSi. Se quería incluir a quienes cumplen exactamente 18. Indica el operador correcto.',[['>=','mayor o igual']],'Cambiar > por >=.','El operador > excluye 18; >= lo incluye.'),
num('p-06','bucles',1,'¿Cuántas veces itera Para i <- 1 Hasta 4 (paso 1)?',4,'Los valores son 1, 2, 3 y 4.'),
mc('p-07','bucles',1,'¿Qué estructura repite mientras una condición sea verdadera?',['Mientras','Si','Segun','Escribir'],'Mientras','Mientras evalúa la condición en cada vuelta.'),
exact('p-08','bucles',2,'predict-code','¿Qué número final se escribe?',['6'],'Se suman 1+2+3 = 6.',code='s <- 0\nPara i <- 1 Hasta 3 Hacer\n  s <- s + i\nFinPara\nEscribir s'),
exact('p-09','bucles',2,'logic','¿Qué valor tiene contador tras dos incrementos desde 0?',['2'],'0 → 1 → 2.'),
exact('p-10','bucles',2,'puzzle','La puerta ejecuta i <- i + 1 partiendo de i=4. ¿Qué valor tiene i después?',['5'],'El nuevo valor es 4 + 1 = 5.')]),
('bases-de-datos','bd-demo','Salas del archivo relacional','Entidades, claves y relaciones elementales en una muestra DEMO.',[
mc('b-01','entidades',1,'En una base de datos de biblioteca, ¿cuál podría ser una entidad?',['Libro','Color azul','Sumar','Verdadero'],'Libro','Un libro es un objeto del dominio sobre el cual se guardan datos.'),
tf('b-02','entidades',1,'Una entidad puede tener atributos como título y año.',True,'Los atributos describen propiedades de una entidad.'),
exact('b-03','entidades',2,'short','¿Cómo se llama el dato que identifica de forma única una fila?',['clave primaria','llave primaria','primary key'],'Una clave primaria distingue inequívocamente cada registro.'),
mc('b-04','entidades',2,'¿Qué atributo conviene como identificador único de Libro?',['Título','ID_Libro','Autor','Género'],'ID_Libro','Un identificador artificial estable evita títulos repetidos.'),
exact('b-05','entidades',2,'puzzle','Un archivo tiene dos libros con el mismo título. ¿Qué atributo evita confundirlos?',['id','id libro','id_libro','identificador'],'Un identificador único permite diferenciarlos.'),
mc('b-06','relaciones',1,'Si un Autor puede escribir muchos Libros y un Libro tiene un Autor, ¿cuál cardinalidad simplificada hay?',['1:N','1:1','N:M','0:0'],'1:N','Un autor se relaciona con muchos libros; cada libro con uno.'),
tf('b-07','relaciones',1,'Una relación N:M suele implementarse mediante una tabla intermedia.',True,'La tabla intermedia almacena los pares de claves foráneas.'),
mc('b-08','relaciones',2,'Estudiante y Curso con inscripciones múltiples en ambos sentidos es...',['1:1','1:N','N:M','Sin relación'],'N:M','Varios estudiantes cursan varios cursos.'),
exact('b-09','relaciones',2,'short','¿Qué tipo de clave referencia la clave primaria de otra tabla?',['clave foránea','llave foránea','foreign key'],'La clave foránea enlaza tablas.'),
exact('b-10','relaciones',2,'puzzle','Entre Estudiante y Curso con cardinalidad N:M, escribe una posible tabla intermedia.',['inscripcion','inscripciones','matricula','matriculas'],'Inscripción puede guardar las claves de estudiante y curso.')])]
for folder,uid,title,description,exercises in units:
 payload={'schemaVersion':1,'id':uid,'subject':folder,'title':title,'description':description,'order':1,'demo':True,'exercises':exercises}
 (root/folder/(uid+'.json')).write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf8')

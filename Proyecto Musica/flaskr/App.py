from flaskr import create_app
from .modelos import db, Usuario, Album, Medio,Cancion


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#prueba

with app.app_context():
    u = Usuario(nombre_usuario='juan', contrasena='12345')
    a = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    c = Cancion(titulo='mi song', minutos=1, segundos=15, interprete='Marco Aurelio')
    u.albumes.append(a)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print(Album.query.all())
    print(Album.query.all()[0].canciones)
    print(Cancion.query.all())
    db.session.delete(a)
    print(Cancion.query.all())
    print(Album.query.all())


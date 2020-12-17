from werkzeug.security import generate_password_hash
from app.models import db, User, League, League_User


def seed_dumb_friends_league():

    demo = User(name='Demo', email='demo@aa.io',
                password='password')
    demodrafter = User(name='DemoDraft', email='demodraft@aa.io',
                       password='password')
    isaac = User(name='Isaac', email='isaac@aa.io',
                 password='password')
    mitch = User(name='Mitch', email='mitch@aa.io',
                 password='password')
    patrick = User(name='Patrick', email='patrick@aa.io',
                   password='password')
    ryan = User(name='Ryan', email='ryan@aa.io',
                password='password')
    tj = User(name='TJ', email='tj@aa.io',
              password='password')
    will = User(name='Will', email='will@aa.io',
                password='password')

    league = League(name='The Dumb Friends League')
    league.admin = demo

    db.session.add(demo)
    db.session.add(demodrafter)
    db.session.add(isaac)
    db.session.add(mitch)
    db.session.add(patrick)
    db.session.add(ryan)
    db.session.add(tj)
    db.session.add(will)
    db.session.add(league)
    db.session.commit()

    demo_lu = League_User(user_id=demo.id, league_id=league.id)
    demodrafter_lu = League_User(user_id=demodrafter.id, league_id=league.id)
    isaac_lu = League_User(user_id=isaac.id, league_id=league.id)
    mitch_lu = League_User(user_id=mitch.id, league_id=league.id)
    patrick_lu = League_User(user_id=patrick.id, league_id=league.id)
    ryan_lu = League_User(user_id=ryan.id, league_id=league.id)
    tj_lu = League_User(user_id=tj.id, league_id=league.id)
    will_lu = League_User(user_id=will.id, league_id=league.id)


    db.session.add(demo_lu)
    db.session.add(demodrafter_lu)
    db.session.add(isaac_lu)
    db.session.add(mitch_lu)
    db.session.add(patrick_lu)
    db.session.add(ryan_lu)
    db.session.add(tj_lu)
    db.session.add(will_lu)
    db.session.commit()


def undo_dumb_friends_league():
    db.session.execute('TRUNCATE league_users RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE leagues RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()

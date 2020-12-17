from werkzeug.security import generate_password_hash
from app.models import db, User, League, League_User


def seed_league_of_extraordinary_gentlemen():

    demodrafter = User(name='DemoDraft', email='demodraft@aa.io',
                password='password')
    chase = User.query.filter(User.name == 'Chase').one()
    isaac = User.query.filter(User.name == 'Isaac').one()
    mitch = User.query.filter(User.name == 'Mitch').one()
    patrick = User.query.filter(User.name == 'Patrick').one()
    ryan = User.query.filter(User.name == 'Ryan').one()
    tj = User.query.filter(User.name == 'TJ').one()
    will = User.query.filter(User.name == 'Will').one()

    league = League(name='The League of Extraordinary Gentlemen')
    league.admin = demodrafter

    db.session.add(demodrafter)
    db.session.add(league)
    db.session.commit()

    demo_lu = League_User(user_id=demodrafter.id, league_id=league.id)
    chase_lu = League_User(user_id=chase.id, league_id=league.id)
    isaac_lu = League_User(user_id=isaac.id, league_id=league.id)
    mitch_lu = League_User(user_id=mitch.id, league_id=league.id)
    patrick_lu = League_User(user_id=patrick.id, league_id=league.id)
    ryan_lu = League_User(user_id=ryan.id, league_id=league.id)
    tj_lu = League_User(user_id=tj.id, league_id=league.id)
    will_lu = League_User(user_id=will.id, league_id=league.id)

    db.session.add(demo_lu)
    db.session.add(chase_lu)
    db.session.add(isaac_lu)
    db.session.add(mitch_lu)
    db.session.add(patrick_lu)
    db.session.add(ryan_lu)
    db.session.add(tj_lu)
    db.session.add(will_lu)
    db.session.commit()


def undo_league_of_extraordinary_gentlemen():
    db.session.execute('TRUNCATE league_users RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE leagues RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()

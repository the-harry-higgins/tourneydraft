from app.models import db, College


def seed_colleges_2022():
    # Boise_State = College(name='Boise State', logo='Boise_State.gif')
    # Colorado_State = College(name='Colorado State', logo='Colorado_State.gif')
    # Memphis = College(name='Memphis', logo='Memphis.gif')
    # San_Francisco = College(name='San Francisco', logo='San_Francisco.gif')
    # Wyoming = College(name='Wyoming', logo='Wyoming.gif')
    # Indiana = College(name='Indiana', logo='Indiana.gif')
    # Notre_Dame = College(name='Notre Dame', logo='Notre_Dame.gif')
    # UAB = College(name='UAB', logo='UAB.gif')
    # Richmond = College(name='Richmond', logo='Richmond.gif')
    # Chattanooga = College(name='Chattanooga', logo='Chattanooga.gif')
    # Akron = College(name='Akron', logo='Akron.gif')
    # Longwood = College(name='Longwood', logo='Longwood.gif')
    # Montana_State = College(name='Montana State', logo='Montana_State.gif')
    # Delaware = College(name='Delaware', logo='Delaware.gif')
    # Saint_Peters = College(name='Saint Peter\'s', logo='Saint_Peters.gif')
    # Jacksonville_State = College(name='Jacksonville State', logo='Jacksonville_State.gif')
    # Bryant = College(name='Bryant', logo='Bryant.gif')
    # Texas_AM_CC = College(name='Texas A&M C.C.', logo='Texas_AM_CC.gif')
    # Norfolk_State = College(name='Norfolk State', logo='Norfolk_State.gif')

    # db.session.add(Akron)
    # db.session.add(Boise_State)
    # db.session.add(Bryant)
    # db.session.add(Chattanooga)
    # db.session.add(Colorado_State)
    # db.session.add(Delaware)
    # db.session.add(Indiana)
    # db.session.add(Jacksonville_State)
    # db.session.add(Longwood)
    # db.session.add(Memphis)
    # db.session.add(Montana_State)
    # db.session.add(Notre_Dame)
    # db.session.add(Richmond)
    # db.session.add(Saint_Peters)
    # db.session.add(San_Francisco)
    # db.session.add(Texas_AM_CC)
    # db.session.add(UAB)
    # db.session.add(Wyoming)
    # db.session.add(Norfolk_State)

    db.session.commit()


def undo_colleges_2022():
    db.session.commit()

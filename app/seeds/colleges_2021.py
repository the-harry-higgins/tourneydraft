from app.models import db, College


def seed_colleges_2021():
    Norfolk_State = College(name='Norfolk St.', logo='Norfolk_State.gif')
    Appalachian_State = College(
        name='Appalachian St.', logo='Appalachian_State')
    UCSB = College(name='UCSB', logo='UCSB.gif')
    Ohio = College(name='Ohio', logo='Ohio.gif')
    USC = College(name='USC', logo='USC.gif')
    Drake = College(name='Drake', logo='Drake.gif')
    Eastern_Washington = College(
        name='Eastern Washington', logo='Eastern_Washington.gif')
    Grand_Canyon = College(name='Grand Canyon', logo='Grand_Canyon.gif')
    Mount_St_Marys = College(name='Mount St. Mary\'s',
                             logo='Mount_St_Marys.gif')
    Colorado = College(name='Colorado', logo='Colorado.gif')
    Georgetown = College(name='Georgetown', logo='Georgetown.gif')
    BYU = College(name='BYU', logo='BYU.gif')
    UCONN = College(name='UCONN', logo='UCONN.gif')
    Hartford = College(name='Hartford', logo='Hartford.gif')
    Winthrop = College(name='Winthrop', logo='Winthrop.gif')
    North_Texas = College(name='North Texas', logo='North_Texas.gif')
    Oral_Roberts = College(name='Oral Roberts', logo='Oral_Roberts.gif')
    Illinois = College(name='Illinois', logo='Illinois.gif')
    Drexel = College(name='Drexel', logo='Drexel.gif')
    Georgia_Tech = College(name='Georgia Tech', logo='Georgia_Tech.gif')
    Oregon_State = College(name='Oregon State', logo='Oregon_State.gif')
    Oklahoma_State = College(name='Oklahoma State', logo='Oklahoma_State.gif')
    Morehead_State = College(name='Morehead State', logo='Morehead_State.gif')
    Rutgers = College(name='Rutgers', logo='Rutgers.gif')
    Cleveland_State = College(name='Cleveland State',
                              logo='Cleveland_State.gif')

    db.session.add(Norfolk_State)
    db.session.add(Appalachian_State)
    db.session.add(UCSB)
    db.session.add(Ohio)
    db.session.add(USC)
    db.session.add(Drake)
    db.session.add(Eastern_Washington)
    db.session.add(Grand_Canyon)
    db.session.add(Mount_St_Marys)
    db.session.add(Colorado)
    db.session.add(Georgetown)
    db.session.add(BYU)
    db.session.add(UCONN)
    db.session.add(Hartford)
    db.session.add(Winthrop)
    db.session.add(North_Texas)
    db.session.add(Oral_Roberts)
    db.session.add(Illinois)
    db.session.add(Drexel)
    db.session.add(Georgia_Tech)
    db.session.add(Oregon_State)
    db.session.add(Oklahoma_State)
    db.session.add(Morehead_State)
    db.session.add(Rutgers)
    db.session.add(Cleveland_State)

    db.session.commit()


def undo_colleges_2021():
    db.session.commit()

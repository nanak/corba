import CORBA
import Caesar

orb = CORBA.ORB_init()
o = orb.string_to_object("corbaloc::host.example.com/caesar")
o = o._narrow(Caesar.CaesarCipher)
print o.encrypt("Hallo das ist ein Test")

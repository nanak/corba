import CORBA
import Caesar

orb = CORBA.ORB_init()
o = orb.string_to_object("IOR:010000001c00000049444c3a4361657361722f4361657361724369706865723a312e3000010000000000000060000000010102000900000031302e302e302e35000032830e000000fee2d28f5100001820000000000000000200000000000000080000000100000000545441010000001c00000001000000010001000100000001000105090101000100000009010100")
o = o._narrow(Caesar.CaesarCipher)
print o.encrypt("Hallo das ist ein Test")

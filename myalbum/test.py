import sae
import sae.storage
from sinastorage.bucket import SCSBucket, ACL
import pdb

def storeImage(imgSrc):
    sinastorage.setDefaultAppInfo('1cjfyo5kQPdnsI3cUc6W',
                                  'a3c139370a3509f269331930515729747573aa10')
    s = SCSBucket('dj-images')  # not dj_images
    adl = {}
    acl[ACL.ACL_GROUP_ANONYMOUSE] = [ACL.ACL_READ]

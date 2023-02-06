import datetime
from base64 import b64decode
from datetime import timedelta
from flask import Flask, request, render_template, redirect, flash, session, jsonify, make_response, url_for, json
import random
import os
import hmac
import hashlib
import sqlite3
import pickle
from apscheduler.schedulers.background import BackgroundScheduler
import logging
from pyChatGPT import ChatGPT
app = Flask(__name__)
app.secret_key = 'laclé'
app.config["SESSION_TYPE"]="filesystem"
'''
@app.route('/')
def main():
        return render_template("acceuilnotlogin.html")







if __name__ == '__main__':
    app.run()'''

session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..SVieIOrQPTB3SnDJ.zuoPfReb9QzrzWc7_8LIS-YRAtZkIdIIX9XdV5l5ZU2BI_KevvbZUVv_Rll60KSNAUN5cd_msYs34CVVuF7i-hEyZSMXlqJ_K7iOIfdgGZ7PXnSsG9-CGOC4RumU2y5nEoybeugQS3r29n50GCe0sNHeg_Gbd4xQk40_kTLWNE2gVlbRomBZbqV41gu_avwj5Wt7JG4u_M1CYwF2xGvalkYYroaOFKil8-kgO7wgyydM8NMQPm_T2kyN006jRhPHVWGNPF39gnUnT23cScb7nTbokWjvUadCX57mcnoRkSUqEkNYtLatDGyOPscwYDsFTlBdqfFmAzk7wUXCOuLiLNbOMv9O35ORS8A-yw0DU_is93WLU8_aN8ToNtWjJQT_lBdkuVvw-dzujSSNA_gIy536D0d9KKtcQQsOCVHz72iJfNsfnB-kAdTzUAAKdtWdTZVERJtDeYSUhIqqaUdKAk1PLDn4uCM5BwGNLZ45vLz4hRBfAA_zvC_D9EVeaA6Mqky5-wt_CdBCwc_KArC7JksKRjDu_3MoTEZM_rLBkdVibI25S7j0euLUvPb5RGpBoYnuCUDXUWF-nWHJA0wjU2h9SFQ6LUH9iGN-lg1tercC2t-ahQMco31T9tgEcp8ByEKGlDLXbnBDc19SU40vc7T-iwgsbT_4Utnk5uVG042RoCzVbEpnAJB6ezhSzWlRuwvx51ZrWEedCisP1zdqUBYKI4IQLooq27XuU9iNOQ-sYOKVeB0mHZzRUcMVpbpsv5oZ4pnmW4j5n7Kwzopnh5CjbC-0jtX2kA_FKP4SnyWJK8YUB8zmJUKU3LXgNdeTiGcP0zPcMnEsCh0H_hkcUCDF3tMYQ1i00Jf7B3nDAMA0hzaljEM7KmZz9HbHLjEr6O0jRz9lLx4sYkCGPZ5ewXbzO3RxLOjrZ__6cMmpVPDguIJTFxwXUBp2pXGvR2oPlGPkeRljK8UDCisZWVa2TH3eg1zr3ircsR-_nFI8wcyOSAxm7yA1KEmCoB9uCnlRjHFBnR6DctLzkmxsyJOcQHRV9mSuMBbYOQX9GpDyp94z6tEe9TFHqs5_8Sjp9RgIWqDpIQ1OLMrCi0twWlfHA75A6lgaFYFN3ZgZAhYXLJf1M-dX9tD2ju1UJQpj4vPPO82pJWDvLgeC1x06M32A2xQ5RMlMRKpI_rYj2g0Lvm-yZtGmXLQcAh0BV1AbYnqGgiBrC6xNsKeK_GXIkk4RhtJMjFLq30j5mtqUZXavLcOhzXa5mMsTIRDn3VzKYoyKgXU9iYsg9oCYMhRvf4fVgCH_h-pFdbiXEyP3Zy6_OydaxwpMsprHgbeVSEgeaqpEYX4rvroYbfQho9cD0G5d853ySgLG2LDcgpm51N4Du5gk6dVfyHS7TuHNecTIZWgQQNRU7wnSNH4FJ0co4tU7lESrf41U0vGrB37rSaFH2qh1TAF78mie2cSRCfJWOEjHruE6sLt0Z17SgE5IT14_-yUAnCkVtA6-xQZyqKbCcUjDrhGZey55ij0dgMlp0JCwwvDo4Y7FoW0VJc5CAzgGwWXAFjYk68At0dw4n49hBK1fCMqOCzq6n1244eIAwi708Sg9XhgXNKhN6s46_hczHwLYsNRcBtzaCBWXGY3fuAYRG1KHZDKVFsDh5ya3NA-CGy7ABbHUW2l8rhx2N23ELAmWf_fWaR4Xg6BQctw8_i6HDg2zOTQJAbEziDzVWvDRBgbjRUzQ9wI_rYRINnDaB0ENh0FYVnammfPwEA4rXVUmk08wN50rCp_r0x8t8NsPkwGlXYth89_UUsX6pvSYZMIdVXkCFuIlVdwl2kY7SfPi8DGaq1pZPdGRHG59e7lzoJ9rPG6Jk_DeD9FCp1zu537WCJj9pu9UMmBvif0U1f8BGpHF0tm6SAdtUJnSyCBnlklZqpE_oRSHGF3qMus6WvjratiGeUe26hQY3je_jumrB18rOyWjaEe9tERnRENTMat4zasgPH9vRT67ZlxeEWvh53s76MC5RkJLc-zz0g96XwxCtdmOyxumxi_6XRbVvcGdcdfVCxFv1J9nsUZWLT_Sy0lnmrg8WS1Kr6Obyr5UnNOa4lzJOdSY9EE5-2gPmIh9R8NjA2oz9p7jaqzDSbx65jo0xWlggbteM0cw66VwjOScm1Ejk_ZvmULVnBiiQoyZ4-Vdn0miZEjUzpKppfVxZyUjgwqFLS8Xl_mM63bSIXrTeguRVGJPTflxiomKUa0BvU5UipBeA62gaGvYDySnke2_6wGdNcHDaMTu7l34eHa9RMT-CZmDdHlY3DXXrAKLEH4YBCjzQNTCf3pRYVYwoBqB8msDUZq_S-Ef4wf4SHKeHT3piIoJgXhF7WcUug8zQmkMf7DLnohKdJhPApXdUW_rOIHIrlSuJmfNfg7dXnzE_MJgDzjkX9I3S43IgYfz6WizuCRv7Hv76siZm3wlQIAceNHuspJmSKyzFpUCRNLb1I3nwVyyi1PqVJ3d6YGhxxfRi63v-F8YJkdVECEIsSemtH_AHAQudkZj33TGbEDGORJBrYZNxzACItznD9-7aFaRzcKfWGptUwk4LI49V-uLk21krNoLwRyndOgbc_VWgVGS8C-x.cw2dmS88PPKlr_JiOKTgBg'  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
api = ChatGPT(session_token)  # auth with session token

resp = api.send_message('Génère un exercice d\'anglais')
print(resp['message'])

api.reset_conversation()  # reset the conversation

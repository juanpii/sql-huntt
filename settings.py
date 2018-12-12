# ================================================
#	Settings
# ================================================
# Name
V_NAME = "SQLHuntt"
V_NAME_DEV = "Juanpii"
V_WEBSITE = "http://juan-dev.com/"
# Examples
E_URL_GET = "https://website.com/?a=1"
E_URL_WITH_SQLI = "https://website.com/?a=0 UNION SELECT 1XX,2XX,3XX,4XX;#"
E_URL_WITH_SQLI_LIMIT = "https://website.com/?a=0 UNION SELECT 1,2 LIMIT 1,1;#"
# General Usage
C_URL = "-u"
C_HELP = "-h"
C_HELP_2 = "-help"
C_FULL_HELP = "--full-help"
# Option Attacks
C_UNION = "--union"
C_UNION_LIMIT = "--union-limit"
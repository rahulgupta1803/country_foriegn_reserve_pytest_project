from objects.forieng_reserve_page import Foreign_Reserve
from utilities.xlutilis import WriteData


class Test_Foreign_Reserve():
    fpath = "D:\\credence\\country_foriegn_reserve_pytest_project\\excel\\foreign_reserve.xlsx"


    def test_foreign(self,setup):
        self.driver = setup
        self.frp = Foreign_Reserve(self.driver)
        self.frp.scroll()
        rl = self.frp.Row_length()
        cl = self.frp.Col_length()
        print(f"Row length : {rl}")
        print(f"Column length : {cl}")
        for c in range(1,cl+1):
            WriteData(self.fpath, 'Sheet1', 1, c, self.frp.Header(c))
            for r in range(1,rl+1):
                WriteData(self.fpath, 'Sheet1',r+1, c, self.frp.iteration(r,c))
        print('Web table extraction is completed')
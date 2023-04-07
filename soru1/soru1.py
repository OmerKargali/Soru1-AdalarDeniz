from typing import List;

        # Ömer KARGALI
        # 1220505069

class AdalarDenizi:
    def AdaNumarası(self, grid: List[List[str]]) -> int:
        SatırNo,SutunNo,AdaNo = len(grid), len(grid[0]),0
        ziyaret = set()
        
        def AdaBul(satır,sutun):
            # Buradaki kısmı ziyaret edilen kısma ekler.
            ziyaret.add((satır,sutun))
            # Sıra sıra bu hücrenin tüm komşularını toplar. (Sol, sağ, üst, alt)
            
            # Burada yer alan ilk rakam satırı belirtirken, ikinci rakam sütun'u belirtir.
            Komsular = [[0,-1], [0,1],[-1,0],[1,0]]
            
            for Satırid,Sutunid in Komsular:

                # Burada yer alan indeks değeri sınırlar içerisinde ve string değeri yani 
                # Komşu değeri == 1 konumunda tutuluyorsa ve bu kısım daha önce ziyaret edilmemiş ise
                # Belirli bir komşuyu ziyaret et
               
                if 0 <= (sutun+Sutunid) < SatırNo and 0 <= (satır+Satırid ) < SatırNo and grid[satır+Satırid][sutun+Sutunid] == "1" and (row+row_id,col+col_id) not in visited:
                    AdaBul(satır+Satırid,sutun+Sutunid)

        for satır in range(SatırNo):
            for sutun in range(SatırNo):
                # Eğer ziyaret edilmemişse her hücre grubunu çağırır.

                if grid[satır][sutun] == "1" and (satır,sutun) not in ziyaret:
                    AdaBul(satır,sutun)
                    
                    # AdaBul fonksiyonu ilerlemesini döndürdüyse artırır
                    # Çünkü bu, bir dizi sürekli hücrenin geçtiği anlamına gelmektedir.
                   
                    AdaNo += 1
        return AdaNo
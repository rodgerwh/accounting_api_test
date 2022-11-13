Задание:   
1. Напишите запрос, который подсчитает какое количество ноутбуков представлено в каждом бренде. Отсортируйте данные по убыванию.
РЕШЕНИЕ: SELECT brand_id, COUNT(brand_id) FROM notebooks_notebook GROUP BY brand_id ORDER BY count DESC;

2. Вам необходимо выделить группы ноутбуков по размерам. Для этого размеры предварительно нужно округлить в большую сторону до ближайшего 0 или 5 и затем сгруппировать по одинаковым размерам, подсчитав количество ноутбуков в каждой группе. Отсортируйте данные по размерам.
SELECT ROUND(CAST(width AS numeric)*2, -1)/2 as width_r, ROUND(CAST(depth AS numeric)*2, -1)/2 as depth_r, ROUND(CAST(height AS numeric)*2, -1)/2 as height_r, COUNT(*) FROM notebooks_notebook GROUP BY width_r, depth_r, height_r ORDER BY width_r, depth_r, height_r;

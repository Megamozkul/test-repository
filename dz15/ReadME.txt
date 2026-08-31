Схема работы кода: В папке data/raw лежит файл "train.csv"- датасет Титаника.
При запуске snakefile (snakemake --cores 4 ) алгоритм должен выполняться следующим образом
1)За таргет берется колонка survived и сохраняется в data/iterim
2) в папке data/processed  появляется обработанный датасет после preprocesinga и разбитые на тест и трэйн данные.
3)модели для обучения находятся в папке forecast.Там же происходит обучение и как результат -файлы csv с y_pred.
4)Подсчет метрик и добавление их в таблицу docker происходит в папке reports.

Теперь про docker.

Я не могу проверить "воспроизводимость" т.к имею один компьютер, поэтому тут два варианта:

Вариант 1: запустить контейнер docker и создать таблицу  вручную : 

docker exec -it my-postgres psql -U postgres -d postgres -c "
CREATE TABLE IF NOT EXISTS model_metrics (
    uid SERIAL PRIMARY KEY,
    model_name VARCHAR(100) NOT NULL,
    accuracy NUMERIC(5,4) NOT NULL,
    precision NUMERIC(5,4) NOT NULL,
    recall NUMERIC(5,4) NOT NULL,
    f1_score NUMERIC(5,4) NOT NULL
);"
Вариант 2: создал файл docker-compose.yml и create_model_metrics.sql  в папке schema.После команды  "docker compose up -d" PostgreSQL должен автоматически выполнить все .sql файлы из ./schema, и таблица model_metrics создастся сама
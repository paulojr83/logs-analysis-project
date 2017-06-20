## Select to get list of errors for monthers##
PERCENTAGE_ERROR ="select x.time, x.percentage_error || '%'  as erros from ("\
                        " select"\
                        " round( (y.count_error * 100 ) / y.total , 2) as percentage_error,"\
                        " round( (y.count_ok * 100 ) / y.total , 2) as percentage_ok,"\
                        " y.total,"\
                        " y.time from ("\
                        " select sum(x.error) count_error, sum(x.ok) count_ok, (sum(x.error)  + sum(x.ok) ) as total, x.time from ("\
                        " select"\
                        " ( case when status != '200 OK' then 1 else 0 end) as error,"\
                        " ( case when status = '200 OK' then 1 else 0 end) as ok,"\
                        " to_char(time, 'Mon DD, YYYY') as time"\
                        " from log"\
                        ") x group by x.time"\
                        ") y"\
                        ") x where x.percentage_error > 1"

## Select to get three must popular article, show title and amount##
MOST_POPULAR_ARTICLE = "select x.title, count(1) as amount from ( " \
                "SELECT a.title FROM articles a " \
                "join authors b on(a.author = b.id) " \
                "join log c on(c.path = '/article/' ||a.slug) " \
                "where c.status = '200 OK' " \
                ") x group by x.title order by 2 desc limit 3;"

## Select to get three must populars authors, show author name and amount##
MOST_POPULAR_AUTHOR = " select x.author , count(1) as qtd from (" \
                      " SELECT b.name as author" \
                      " FROM articles a join authors b on(a.author = b.id)" \
                      " join log c on(c.path = '/article/' ||a.slug)" \
                      " ) x group by x.author order by 2 desc limit 3;"

## Select to get amount article by author, show the title, time and amount##
AMOUNT_ARTICLE_BY_AUTHOR ="select x.title, x.time, count(1) as amount from ( " \
                          " SELECT a.title,b.name, a.lead, to_char(c.time, 'Mon DD, YYYY') as time " \
                          " FROM articles a join authors b on(a.author = b.id)" \
                          " join log c on(c.path = '/article/' ||a.slug)" \
                          " where c.status = '200 OK'" \
                          " ) x where x.name = '%s' group by x.title, x.time order by 1, 2, 3 desc;"
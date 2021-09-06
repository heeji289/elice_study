# 프로그래머스 SQL 고득점 Kit

### 알아둘 것 🎁
- SELECT 할 때 순서 (지켜야함, 안 그러면 에러 발생)
    ```sql
    SELECT 컬럼명
    FROM 테이블명
    -- 다음 네 개 순서 주의 
    WHERE 테이블 조건
    GROUP BY 컬럼명
    HAVING 그룹 조건
    ORDER BY
    ```

- 사용자 정의 변수
    ```sql
    --- 사용자 정의 변수 선언 및 초기화
    SET @foo = 1; 혹은 SET @foo := 1;
    SELECT @foo := 1 FROM tables;

    -- 사용자 정의 변수 사용법
    SET @start = 15, @finish = 20;
    SELECT * FROM employee 
    WHERE id BETWEEN @start AND @finish;
    ```
- 컬럼이 null일 때 대체값을 넣어주는 법
    ```sql
    -- IFNULL 활용
    SELECT IFNULL(Column명, "Null일 경우 대체 값") FROM 테이블명;
    -- CASE 활용
    SELECT 
    CASE
        WHEN NAME IS NULL THEN "No name"
        ELSE NAME
    END as NAME
    FROM ANIMAL_INS
    -- COALESCE (모든 SQL에서 사용가능)
    SELECT COALESCE(NAME, "No name")
    FROM ANIMAL_INS
    ```

## SELECT
- 문제에 사용되는 테이블 정보

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다.   
`ANIMAL_INS` 테이블 구조는 다음과 같으며,   
`ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

|NAME|	TYPE|	NULLABLE|
|------|---|---|
|ANIMAL_ID|	VARCHAR(N)|	FALSE|
|ANIMAL_TYPE|	VARCHAR(N)|	FALSE|
|DATETIME|	DATETIME	|FALSE|
|INTAKE_CONDITION|	VARCHAR(N)|	FALSE|
|NAME|	VARCHAR(N)|	TRUE|
|SEX_UPON_INTAKE|	VARCHAR(N)	|FALSE|

`ANIMAL_OUTS` 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다.  
`ANIMAL_OUTS` 테이블 구조는 다음과 같으며,  
`ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME`는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다.

|NAME|	TYPE	|NULLABLE|
|------|---|---|
|ANIMAL_ID|	VARCHAR(N)|	FALSE|
|ANIMAL_TYPE|	VARCHAR(N)|	FALSE|
|DATETIME|	DATETIME|	FALSE|
|NAME|	VARCHAR(N)|	TRUE|
|SEX_UPON_OUTCOME	|VARCHAR(N)|	FALSE|

### 모든 레코드 조회하기
동물 보호소에 들어온 모든 동물의 정보를 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요.
```sql
SELECT * 
FROM animal_ins
```

### 역순 정렬하기
동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 

```sql
SELECT name, datetime
FROM animal_ins
ORDER BY animal_id DESC
```

### 아픈 동물 찾기
동물 보호소에 들어온 동물 중 아픈 동물의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.
- INTAKE_CONDITION이 Sick 인 경우 = 아픈 경우
```sql
SELECT animal_id, name
FROM animal_ins
WHERE intake_condition = 'Sick'
ORDER BY animal_id
```

### 어린 동물 찾기
동물 보호소에 들어온 동물 중 젊은 동물의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.
- INTAKE_CONDITION이 Aged가 아닌 경우 = 젋음
```sql
SELECT animal_id, name
FROM animal_ins
WHERE intake_condition != 'Aged'
ORDER BY animal_id
```

### 동물의 아이디와 이름
동물 보호소에 들어온 모든 동물의 아이디와 이름을 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요.
```sql
SELECT animal_id, name
FROM animal_ins
ORDER BY animal_id
```

### 여러 기준으로 정렬하기
동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문을 작성해주세요.  
단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.
```sql
-- 여러개 정렬시 콤마로
SELECT animal_id, name, datetime
FROM animal_ins
ORDER BY name, datetime DESC
```

### 상위 n개 레코드
동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요.
```sql
SELECT name
FROM animal_ins
ORDER BY datetime
LIMIT 1
```

## SUM, MAX, MIN

### 최댓값 구하기
가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.
```sql
SELECT MAX(datetime)
FROM animal_ins
```

### 최솟값 구하기
동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.
```sql
SELECT MIN(datetime)
FROM animal_ins
```

### 동물 수 구하기
동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문을 작성해주세요.
```sql
SELECT COUNT(animal_id)
FROM animal_ins
```

### 중복 제거하기
동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.
```sql
SELECT COUNT(DISTINCT name)
FROM animal_ins
```

## GROUP BY

### 고양이와 개는 몇 마리 있을까
동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.
```sql
SELECT animal_type , COUNT(animal_type) count
FROM animal_ins
GROUP BY animal_type
ORDER BY animal_type
```

### 동명 동물 수 찾기
동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.
```sql
SELECT name, COUNT(name) COUNT
FROM animal_ins
GROUP BY name
HAVING COUNT(name) >= 2
ORDER BY name
```

### 입양 시각 구하기(1)
보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
```sql
SELECT HOUR(datetime), COUNT(HOUR(datetime))
FROM animal_outs
WHERE HOUR(datetime) >= 9 AND HOUR(datetime) <= 19
GROUP BY HOUR(datetime)
ORDER BY HOUR(datetime)
```

### 입양 시각 구하기(2) 📌
보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
- 풀이 : 로컬변수를 활용. hour이라는 변수 생성후 HOUR(datetime)이 hour과 같을 때를 고른다
```sql
SET @hour := -1;

SELECT (@hour := @hour + 1) AS HOUR,
    (SELECT COUNT(*)
     FROM animal_outs
     WHERE HOUR(datetime) = @hour
    )AS COUNT
FROM animal_outs
WHERE @hour < 23
```

## IS NULL

### 이름이 없는 동물의 아이디
동물 보호소에 들어온 동물 중, 이름이 없는 채로 들어온 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.
```sql
SELECT animal_id
FROM animal_ins
WHERE name IS NULL
ORDER BY animal_id asc
```

### 이름이 있는 동물의 아이디
동물 보호소에 들어온 동물 중, 이름이 있는 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.
```sql
SELECT animal_id
FROM animal_ins
WHERE name IS NOT NULL
ORDER BY animal_id asc
```

### NULL 처리하기 📌
입양 게시판에 동물 정보를 게시하려 합니다. 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시해 주세요.

```sql
SELECT animal_type, IFNULL(name, 'No name'), sex_upon_intake
FROM animal_ins
```

## JOIN

### 없어진 기록 찾기
- [OUTER JOIN 참고링크](https://rh-cp.tistory.com/44)
천재지변으로 인해 일부 데이터가 유실되었습니다. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
- outs를 기준으로 ins를 join한 후 그 중 ins에 없는 것을 출력
```sql
-- outs엔 있고 ins엔 없는 것
SELECT O.animal_id, O.name
FROM animal_ins I
RIGHT OUTER JOIN animal_outs O
ON I.animal_id = O.animal_id
WHERE I.animal_id IS NULL
ORDER BY I.animal_id
```

### 있었는데요 없었습니다
관리자의 실수로 일부 동물의 입양일이 잘못 입력되었습니다. 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.
- inner join후, datetime을 비교
```sql
SELECT I.animal_id, I.name
FROM animal_ins I
INNER JOIN animal_outs O
ON I.animal_id = O.animal_id
WHERE I.datetime > O.datetime
ORDER BY I.datetime
```

### 오랜 기간 보호한 동물(1) 
아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일 순으로 조회해야 합니다.
- ins를 기준으로 left join을 해준 후, outs에 없는 애들을 선택한다.
```sql
-- 입양 못간 애들 중 오래있었던 3마리
SELECT I.name, I.datetime
FROM animal_ins I
LEFT JOIN animal_outs O
ON I.animal_id = O.animal_id
WHERE O.animal_id IS NULL
ORDER BY I.datetime
LIMIT 3
```

### 보호소에서 중성화한 동물📌
보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다. 보호소에 들어올 당시에는 중성화1되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.
- 중성화를 거치지 않은 동물은 성별 및 중성화 여부에 Intact, 중성화를 거친 동물은 Spayed 또는 Neutered라고 표시되어있습니다. ↩
```sql
SELECT I.animal_id, I.animal_type, I.name
FROM animal_ins I
INNER JOIN animal_outs O
ON I.animal_id = O.animal_id
WHERE I.SEX_UPON_INTAKE LIKE 'Intact%' AND
(O.SEX_UPON_OUTCOME LIKE 'Spayed%' OR O.SEX_UPON_OUTCOME LIKE 'Neutered%')
```
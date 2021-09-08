/*
  베스트 앨범: 자바스크립트 버전입니다.
  로직은 파이썬 코드와 동일합니다. 하지만 코드가 참...더럽게 짜가지고;;

  간단히 설명하면 Object.values은 파이썬의 dict.values와 동일한 친구지만
  객체를 매개변수로 받기 때문에 매개변수로 {'pop': [[500, -3], [700, -1]]} 이런 형태의 객체를 넘겨주기 위한 과정입니다.
  장르로 reduce를 돌리는데 초기값을 빈 객체(obj)를 넘겨서 현재 obj에 해당 장르를 key로 하는 값이 존재하면
  spread operator(맞나?) 이걸로 기존거 + [플레이 수, 음수의 고유넘버]를 obj[genre]에 덮어씌워주고,
  없는 경우 [[플레이 수, 음수의 고유넘버]] 요 형태의 2차원 array 형태로 넣어줍니다.
  그리고나서 희지님이 하셨던 방식과 비슷한 방법을 사용했는데요.
  sort를 할 때 key를 장르별 플레이 수 합으로 해서 sort를 진행했습니다. reduce를 중복 써야해서 sum으로 arrow 함수를 하나 맨들어서 썼습니다.
  그 후 장르별로 내림차 정렬된 결과를 다시 reduce로 돌리는데 이번엔 초기 값으로 빈 array를 넘겨서 현재 장르의 플레이 리스트를 내림차 정렬하고
  그 중 2개의 원소만 골라서 초기값으로 넘긴 빈 array에 하나씩 넣어줍니다.
*/

const solution = (genres, plays) => {
  const sum = (x) => x.reduce((prev, val) => prev + val[0], 0);
  return Object.values(
    genres.reduce((obj, genre, num) => {
      obj[genre] = obj[genre]
        ? [...obj[genre], [plays[num], -num]]
        : [[plays[num], -num]];
      return obj;
    }, {})
  )
    .sort((x, y) => sum(y) - sum(x))
    .reduce((arr, play_list) => {
      play_list
        .sort((x, y) => y[0] - x[0])
        .slice(0, 2)
        .forEach(([_, num]) => arr.push(-num));
      return arr;
    }, []);
};

/*
  위장: 자바스크립트 버전입니다.
  로직은 파이썬 코드와 동일합니다.
*/

// return 한번으로 끝내보고 싶었지만 잘 안되네요;
const solution = (clothes) => {
  const cnt = {};
  clothes.forEach(([_, type]) => (cnt[type] = (cnt[type] || 1) + 1));
  return Object.values(cnt).reduce((prev, next) => prev * next) - 1;
};

// 다른 분의 풀이 중 reduce를 잘 이용해서 리턴 한번으로 끝내버린 코드가 있어서 가져와봤습니다. ㅎㅎ
function solution(clothes) {
  return (
    Object.values(
      clothes.reduce((obj, t) => {
        obj[t[1]] = obj[t[1]] ? obj[t[1]] + 1 : 1;
        return obj;
      }, {})
    ).reduce((a, b) => a * (b + 1), 1) - 1
  );
}

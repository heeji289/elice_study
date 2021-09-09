/*
  풀이요약
    다리를 지나는 트럭 자바스크립트 버전입니다.
    로직은 정규님 파이썬 로직과 비슷하게 해봤습니다.
*/
function solution(bridge_length, weight, truck_weights) {
  let time = 0;
  const bridge = [];
  let current = 0;
  let total = 0;
  let pass = 0;
  while (current < truck_weights.length) {
    ++time;
    if (bridge.length !== 0 && time === bridge[pass][0]) {
      total -= bridge[pass++][1];
    }

    if (total + truck_weights[current] <= weight) {
      total += truck_weights[current];
      bridge.push([bridge_length + time, truck_weights[current++]]);
    }
  }

  return bridge[truck_weights.length - 1][0];
}

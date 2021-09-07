/*
  풀이요약
    풀이 로직은 파이썬 풀이와 동일합니다.
    다만, 아직 자바스크립트에 어떤 라이브러리들이 있는지 없는지 잘 몰라서
    정석대로 Queue를 직접 만들어서 풀어봤습니다ㅎㅎ
    자료 범위가 적어서 자바스크립트 Array 메소드 중에 shift를 이용하면 편하긴하지만
    가끔 직접 만들어서 해보는 것도 괜찮은 것 같아요. 코드가 길어지긴 하지만요😅

    Queue는 function constructor로 정의했고, 기본적으로 queue의 동작에 필요한 속성과 메서드를 정의했습니다.
    필요할 것 같은 것만 구현하고 전부 구현하지는 않았습니다.

    마지막에 shift를 이용한 풀이도 추가해봤습니다.
*/

const Queue = function () {
  this.data = [];
  this.length = 0;
  this.maxSize = 0;
  this.front = 0;
  this.rear = -1;
  this.init = function (size) {
    this.maxSize = size;
  };
  this.enqueue = function (data) {
    if (this.is_full() || data === undefined) {
      return;
    }

    this.rear = this.rear < 0 ? 0 : this.rear;
    this.data[this.rear] = data;
    ++this.rear % this.maxSize;
    ++this.length;
  };
  this.dequeue = function () {
    if (this.is_empty()) {
      return;
    }

    const poped = this.data[this.front];
    ++this.front % this.maxSize;
    --this.length;
    return poped;
  };
  this.is_empty = function () {
    return !this.length;
  };
  this.is_full = function () {
    return this.front === this.rear;
  };
  this.frontValue = function () {
    return this.data[this.front];
  };
};

const solution = (priorities, location) => {
  let answer = 0;
  const compareQ = new Queue();
  const workQ = new Queue();
  compareQ.init(priorities.length);
  workQ.init(priorities.length);

  priorities.forEach((priority, idx) => {
    compareQ.enqueue(priority);
    workQ.enqueue([priority, idx == location]);
  });
  compareQ.data.sort((x, y) => y - x);

  while (!workQ.is_empty()) {
    const [priority, mark] = workQ.dequeue();
    if (priority !== compareQ.frontValue()) {
      workQ.enqueue([priority, mark]);
      continue;
    }

    ++answer;
    if (mark) {
      return answer;
    }
    compareQ.dequeue();
  }
};

// 요건 shift를 썼을 때 간단하게 구현한 코드입니다.
// 실전에선 아마 요렇게 해야곘지요.
const solution = (priorities, location) => {
  const workQ = priorities.map((priority, idx) => [priority, idx === location]);
  const compareQ = priorities.sort((x, y) => y - x);

  let current = 0;
  while (true) {
    const [priority, mark] = workQ.shift();
    if (priority !== compareQ[current]) {
      workQ.push([priority, mark]);
      continue;
    }

    ++current;
    if (mark) {
      return current;
    }
  }
};

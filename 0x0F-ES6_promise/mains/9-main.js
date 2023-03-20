import divideFunction from '../8-try';
import guardrail from '../9-try';

console.log(guardrail(() => divideFunction(10, 2)));
console.log(guardrail(() => divideFunction(10, 0)));

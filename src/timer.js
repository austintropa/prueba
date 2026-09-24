import {recoverTimer} from './store.js';
export function tick(t){if(!t.running)return false;recoverTimer(t);if(t.remaining>0)return false;t.running=false;t.endsAt=0;t.remaining=0;if(t.phase==='focus'){t.completed++;t.phase='break';t.remaining=600}else{t.phase='focus';t.remaining=2700}return true}
export function toggle(t){if(t.running){recoverTimer(t);t.running=false;t.endsAt=0}else{if(t.remaining<=0)t.remaining=t.phase==='focus'?2700:600;t.running=true;t.endsAt=Date.now()+t.remaining*1000}}
export function skip(t){t.running=false;t.endsAt=0;t.phase=t.phase==='focus'?'break':'focus';t.remaining=t.phase==='focus'?2700:600}
export const timeText=n=>`${String(Math.floor(n/60)).padStart(2,'0')}:${String(n%60).padStart(2,'0')}`;

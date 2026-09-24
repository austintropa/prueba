import {ITEMS,xpNeed} from './config.js';
export function item(id){return ITEMS.find(x=>x.id===id)}
export function bonus(s,slot){return item(s.equipment[slot])?.power||0}
export function addXp(s,amount){s.xp+=amount;let levels=0;while(s.xp>=xpNeed(s.level)){s.xp-=xpNeed(s.level);s.level++;levels++;s.hp=maxHp(s)}return levels}
export function maxHp(s){return 32+s.level*3+bonus(s,'armor')*3}
export function chest(s){s.chests++;const roll=Math.random(),rarity=roll<.78?'common':roll<.97?'rare':'epic',pool=ITEMS.filter(i=>i.rarity===rarity),gift=pool[Math.floor(Math.random()*pool.length)];if(s.inventory.includes(gift.id)){s.gold+=rarity==='common'?12:rarity==='rare'?32:70;return {name:`${gift.name} duplicado`,gold:true}}s.inventory.push(gift.id);return gift}

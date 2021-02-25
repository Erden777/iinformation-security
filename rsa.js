function gcd (a, b)
{
   var r;
   while (b>0)
   {
      r=a%b;
      a=b;
      b=r;
   }
   return a;
}

function rel_prime(phi)
{
   var rel=5;
   
   while (gcd(phi,rel)!=1)
      rel++;
   return rel;
}

function power(a, b)
{
   var temp=1, i;
   for(i=1;i<=b;i++)
      temp*=a;
    return temp;
}

function encrypt(N, e, M)
{
   var r,i=0,prod=1,rem_mod=0;
   while (e>0)
   {
      r=e % 2;
      if (i++==0)
         rem_mod=M % N;
      else
         rem_mod=power(rem_mod,2) % N;
      if (r==1)
      {
         prod*=rem_mod;
         prod=prod % N;
      }
      e=parseInt(e/2);
   }
   return prod;
}

function calculate_d(phi,e)
{
   var x,y,x1,x2,y1,y2,temp,r,orig_phi;
   orig_phi=phi;
   x2=1;x1=0;y2=0;y1=1;
   while (e>0)
   {
      temp=parseInt(phi/e);
      r=phi-temp*e;
      x=x2-temp*x1;
      y=y2-temp*y1;
      phi=e;e=r;
      x2=x1;x1=x;
      y2=y1;y1=y;
      if (phi==1)
      {
         y2+=orig_phi;
         break;
      }
   }
   return y2;
}

function decrypt(c, d, N)
{
   var r,i=0,prod=1,rem_mod=0;
   while (d>0)
   {
      r=d % 2;
      if (i++==0)
         rem_mod=c % N;
      else
         rem_mod=power(rem_mod,2) % N;
      if (r==1)
      {
         prod*=rem_mod;
         prod=prod % N;
      }
      d=parseInt(d/2);
   }
   return prod;
}

const alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];

function openNew()
{

   let encrypt = document.getElementsByName("name")[0];
   var p=parseInt(document.Input.p.value);
   var q=parseInt(document.Input.q.value);
   var N=p * q;
   var phi=(p-1)*(q-1);
   var e=rel_prime(phi);
   var d=calculate_d(phi,e);
   const textArr = encrypt.value.split('');
   let res = document.querySelector(".res");
   let res_2 = document.querySelector(".res-2");
   let private_array = [];
   res.innerHTML = "";

   textArr.forEach((elem, i) => {
       const letter = elem.toLowerCase();

       const index = alphabet.indexOf(letter) + 1;

       const text = res.innerHTML;
       let ans = (Math.pow(index, e) % N);

       let finalText = `<div>${text} <span>${letter} ${i}</span> | ${index}^${e}mod${N} =  ${ans}</div>`;
       private_array.push(ans);

       res.innerHTML = finalText;
   });

   console.log(private_array);

   private_array.forEach((elem, i) => {
      console.log(elem)
      let box = document.createElement("div");

      let privateText = `<div> C ${i} </span> | ${elem}^${d}mod${N} =  ${(Math.pow(elem, d) % N)}</div>`;
      box.innerHTML = privateText;

      res_2.appendChild(box);
  })

}

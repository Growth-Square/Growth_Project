if (typeof(window.RadSpellNamespace)=="und\x65\x66\151\x6eed"){window.RadSpellNamespace=new Object(); }RadSpellNamespace.O= function (text){var o=text.replace(/\x0a/gi,"\x3c\x74\145\x6cerikcr\x20/>"); o=o.replace(/\x0d/gi,"<tel\x65riklf /\x3e"); return o; } ; RadSpellNamespace.I= function (text){var o=text.replace(/\x3c\x74\x65\x6c\x65\x72\x69\x6b\x63\x72\s*\x2f\x3e/gi,"\012"); var o=o.replace(/\x3c\x74\x65\x6c\x65\x72\x69\x6b\x6c\x66\s*\x2f\x3e/gi,"\x0d"); return o; } ; function A(U,ownerDocument){ this.Z=U; if (ownerDocument==null){ownerDocument=document; } ; this.ownerDocument=ownerDocument; } ; A.prototype.z= function (){return (this.Z.disabled!= true); } ; A.prototype.W= function (w){var V=(w== true)?"e\x6e\x61ble": "disabl\x65"; this[V](); } ; A.prototype.v= function (){return ""; } ; A.prototype.T= function (){return ""; } ; A.prototype.t= function (){ this.Z.disabled= false; if (this.T()!=""){ this.Z.className=this.T(); } ; } ; A.prototype.S= function (){ this.Z.disabled= true; if (this.v()!=""){ this.Z.className=this.v(); } ; } ; A.prototype.R= function (){return this.Z.style.visibility!="h\x69dden"; } ; A.prototype.r= function (){ this.Z.style.visibility="\x68i\x64\x64en"; } ; A.prototype.Q= function (){return this.Z.style.display; } ; A.prototype.P= function (N){ this.Z.style.display=N; } ; A.prototype.show= function (){ this.Z.style.visibility="\x76isible"; } ; A.n= function (M,m){if (m==null){m=document; } ; if (m.all!=null){return m.all[M]; } ; return m.getElementById(M); } ; function L(){var l= function (Z,ownerDocument){ this.base=A; this.base(Z,ownerDocument); } ; l.prototype=new A(); l.K= function (M,m){var k=A.n(M,m); if (k==null){return null; }else {return new l(k,m); } ; } ; return l; } ; var J=L(); J.prototype.getText= function (){return this.Z.innerHTML; } ; J.prototype.setText= function (caption){ this.Z.innerHTML=caption; } ; J.prototype.H= function (h){ this.Z.onclick=h; };var G=L(); G.prototype.g= function (){return this.Z.options.length; } ; G.prototype.F= function (f,D){var d=new Option(f,D); if (this.Z.options.add!=null){ this.Z.options.add(d); }else { this.Z.options[this.g()]=d; }} ; G.prototype.C= function (){ this.Z.options.length=0; } ; G.prototype.c= function (){return this.Z.selectedIndex; } ; G.prototype.B= function (selected){ this.Z.selectedIndex=selected; } ; G.prototype.getItem= function (index){return this.Z.options[index]; } ; var o0=L(); o0.prototype.getText= function (){return this.Z.value; } ; o0.prototype.setText= function (text){ this.Z.value=text; } ; var O0=L(); O0.prototype.getText= function (){var html=this.l0().innerHTML; return html!=null?html: ""; } ; O0.prototype.setText= function (text){ this.l0().innerHTML=text; } ; O0.prototype.i0= function (){var I0=this.Z.id; var iframe=null; if (this.ownerDocument.frames!=null && this.ownerDocument.frames[I0]!=null){iframe=this.ownerDocument.frames[I0]; } ; if (iframe==null){iframe=A.n(I0,this.ownerDocument); } ; if (iframe.document!=null){return iframe.document; }else {return iframe.contentWindow.document; } ; } ; O0.prototype.l0= function (){return this.i0().body; } ; O0.prototype.o1= function (){var I0=this.Z.id; var iframe=null; if (this.ownerDocument.frames!=null && this.ownerDocument.frames[I0]!=null){return this.ownerDocument.frames[I0]; } ; if (iframe==null){var frame=A.n(I0,this.ownerDocument); return frame.contentWindow; } ; return null; } ; O0.prototype.O1= function (){return typeof(this.l0().contentEditable)!="\165\x6e\x64\x65\x66ined"; } ; O0.prototype.l1= function (i1){if (this.O1()){ this.l0().contentEditable=i1; } ; } ; O0.prototype.I1= function (){if (!this.O1()){return false; }else {return this.l0().contentEditable=="\164\x72ue" || this.l0().contentEditable== true; } ; } ; var o2=L(); o2.prototype.v= function (){return "ButtonD\x69sable\x64"; } ; o2.prototype.T= function (){return "Bu\x74ton"; } ; o2.prototype.O2= function (){return this.Z.innerHTML; } ; o2.prototype.l2= function (caption){ this.Z.innerHTML=caption; } ;
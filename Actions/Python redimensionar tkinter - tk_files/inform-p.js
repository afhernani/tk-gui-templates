$(document).ready(function(){
  // код для вывода адсенс
   var adsens = Array(
            '<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-2878089661277044" data-ad-slot="4087598952" data-ad-format="link"></ins><script>(adsbygoogle = window.adsbygoogle || []).push({});</script>',
            '<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><ins class="adsbygoogle" style="display:block; text-align:center;"     data-ad-layout="in-article" data-ad-format="fluid" data-ad-client="ca-pub-2878089661277044" data-ad-slot="4557073480"></ins><script>(adsbygoogle = window.adsbygoogle || []).push({});</script>',
            '<center><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><ins class="adsbygoogle" style="display:inline-block;width:336px;height:280px" data-ad-client="ca-pub-2878089661277044" data-ad-slot="6576237334"></ins><script>(adsbygoogle = window.adsbygoogle || []).push({});</script></center>',
					  '<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><ins class="adsbygoogle adslot_1"style="display: inline-block;" data-ad-client="ca-pub-2878089661277044" data-ad-slot="7962810935"></ins><script>(adsbygoogle = window.adsbygoogle || []).push({});</script>',
					  '<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><ins class="adsbygoogle adslot_1"style="display: inline-block;" data-ad-client="ca-pub-2878089661277044" data-ad-slot="7962810935"></ins><script>(adsbygoogle = window.adsbygoogle || []).push({});</script>'
					  );					
  
  // Вставлям код с текстовой рекламой, можно уменьшать или увеличивать кол-во значений в массиве
  var text_ads = Array('', 
					   '', 
					   '',
					   ''
					   );
                  
                  //Количество символов через которое вставлять рекламу;
                 var qtyAdd = 100;// От скольки вставлять
                  var qtyAddTo = 1500; // На сколько шагать
  //Вставляем рекламнный комментарий
  var comment_ads = 'Здесь будет код комментария';

  //Включение/Выключение рекламного комментария; true - включен, false - выключен
  var text_tubmler = false;
  var comment_tubmler = false;
  var img_tubmler = false;
  var adsens_tubmler = false;
  var adsens_tubmler2 = true;
                  
//Код для вставки в картинку
   var img_ads = '';
//Дописать класс блока для картинки
   var class_img = 'adsImg';
  //Контейнер в котором храниться статья; Класс указывается с точкой, а ид с решеткой (как в стилях)
  var container = '.post_content';
  
  //Контейнер для комментария
  var containerComments = '.comments';
   //Тег после которого вставлять комментарий
    var tegComment ='';
//Начало обработки дом
  var qtyTegP = $(container).children('div');
                  //console.log(qtyTegP);
  var qtyTegUl = $(container).find('ul');
                //  console.log(qtyTegUl);
 var qtyTegOl = $(container).find('ol');
 // console.log(qtyTegOl);
//Вставка adnsens в центр стать
				 if(adsens_tubmler){
                  var heightOfConteiner = $(container).height()/2;
                 // console.log(heightOfConteiner);
                  //Цикл для поиска центра по тегу <p>
					qtyTegP.each(function(){
                               var positionFromTopTegP = $(this).offset().top;
                               if(positionFromTopTegP >= heightOfConteiner){
                               $(this).after(adsens);
                               //console.log('Высота тега <p>: '+positionFromTopTegP);
                                                        return false;
                               }
                               });
									}
									
//Вставка adnsens в центр стать
				 if(adsens_tubmler2){
                var textLength = $(container).text().length;
                  var lengthOFkids = 0;
                  var i = 0;
                  //Найдем всех детей блока и посчитаем кол-во символов у них
                  $(container).children().each(function(){
                                            lengthOFkids = lengthOFkids + $(this).text().length;
                                               if(lengthOFkids > qtyAdd){
                                               $(this).after(adsens[i]);
                                               qtyAdd = qtyAdd+qtyAddTo;
                                               if(i == (adsens.length-1)){
                                               i = 0;
                                             // console.log(i);
                                               }
                                               else{
                                               i++
                                               //console.log(i);
                                               }
                                               //console.log(lengthOFkids+' - '+text_ads[i]);
                                               }
                                               
                                                       });
									}
                  
//Вставка текстовой рекламы
				if(text_tubmler){
                  var textLength = $(container).text().length;
                  var lengthOFkids = 0;
                  var i = 0;
                  //Найдем всех детей блока и посчитаем кол-во символов у них
                  $(container).children().each(function(){
                                            lengthOFkids = lengthOFkids + $(this).text().length;
                                               if(lengthOFkids > qtyAdd){
                                               $(this).after(text_ads[i]);
                                               qtyAdd = qtyAdd+qtyAddTo;
                                               if(i == (text_ads.length-1)){
                                               i = 0;
                                             // console.log(i);
                                               }
                                               else{
                                               i++
                                               //console.log(i);
                                               }
                                               //console.log(lengthOFkids+' - '+text_ads[i]);
                                               }
                                               
                                                       });
				}
//Вставка Комментария
                  //Проверяем включенна ли функция вставки комментария
                  if(comment_tubmler){
                  //Если комментарии включены то находи блок для комментарив и вставляем первый комментариий
                  $(containerComments+' '+tegComment+':first-child').after(comment_ads);
                  }
//Вставляем рекламу в картинку
				  if(img_tubmler){
                    var i = 0;
                  $(container).find('img').each(function(){
                                                $(this).attr('data-indexImg', i++);
                                                                     $(this).after('<div class="'+class_img+'">'+img_ads+'</div>');
                                                
                                                    });
                      $('.'+class_img).hide();
                  $('img').hover(function(){
                                                       var inde = $(this).attr('data-indeximg');
                                                       $('.'+class_img).eq(inde).show();
                                 $('.'+class_img).hover(function(){
                                                        $(this).show();
                                                        },function(){
                                                        $(this).hide()});
                                                       },function(){
                                                               var inde = $(this).attr('data-indeximg');
                                                       $('.'+class_img).eq(inde).hide();
                                                       })
                  $('.'+class_img).click(function(e){
                                e.preventDefault();
                                LinkClic= $(this).find('a').attr('href');
                                window.open( LinkClic,'_blank');
                                });
				  }
                    });
//Плавающий блок
(function ($) {
	$.fn.fixedblock = function (options, callbackdown, callbackup) {
		var opt = $.extend({
			speed: 'fast',
			fooId: '',
			minWidth: 0
		}, options);
		return this.each(function(){
			var e = this;
			var y = $(e).offset().top;
			var b = false;
			var w = $(e).width();
			var min = true;
			if (opt.minWidth && typeof (opt.minWidth) === 'number') {
				$(window).resize(function(){
					min = $(window).width() > opt.minWidth;
					$(window).scroll();
				});
			}
			$(window).scroll(function() {
				if (min) {
					if (y - $(window).scrollTop() <= 0) {
						if (!b) {
							b = true;
							$(e).css({
								position: 'fixed',
								top: 15,
								width: w + 'px'
							});
							if (callbackdown && typeof (callbackdown) === 'function') callbackdown(e, opt);
						}
					} else {
						if (b) {
							b = false;
							$(e).css({
								position: 'relative',
								top: 0
							});
							if (callbackup && typeof (callbackup) === 'function') callbackup(e, opt);
						}
					}
				}
			});
			$(window).scroll();
		});
	}
})(jQuery);

$(window).load(function(){ // ждем загрузки страницы и всех картинок
    $('#block').fixedblock();
	$('#block2').fixedblock();
  });
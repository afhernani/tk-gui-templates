$(function() {

	


	/*	SubMenu  */

	$('.cat-menu-btn').on('click', function () {
        $(this).parents('.nav').find('.cat-menu-list').toggle();
        return false;
    });


	/*	Login  */

	$('.header-controls > .login-btn').on('click', function () {
        $(this).parents('.header-controls').find('.login_block').toggle();
        return false;
    });



	/*	Menu  */

	$('.wrap > .nav-btn').on('click', function () {
        $(this).parents('.wrap').find('.nav').toggle();
        return false;
    });


	/*	Close all   */

	$(document).on('click', function(e) {

		if (!$(e.target).parents().hasClass('header-controls')) {
			$('.login_block').hide();
		}
		if (!$(e.target).parents().hasClass('header>wrap')) {
			$('.cat-menu-list').hide();
		}
		if (!$(e.target).parents().hasClass('header>wrap') && $('body').width() < 960) {
			$('.nav').hide();
		}
	});

		
});


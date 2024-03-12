<div class="container-side-nav-bar">
	<h1 class="nav-title">A-Hub</h1>
	<h1 class="nav-title-sub">Analytical hub</h1>
	<div class="side-nav-bar">
		<div class="item-nav-container">
			<a href="/">
				<i class="fa-solid fa-house item-icon"></i><span class="item-nav-desc">Home</span>
			</a>
		</div>
		<div class="item-nav-container">
			<a href="/analytics">
				<i class="fa-solid fa-database item-icon"></i><span class="item-nav-desc">Dados</span>
			</a>
		</div>
		<div class="item-nav-container">
			<a href="/">
				<i class="fa-solid fa-user item-icon"></i><span class="item-nav-desc">User</span>
			</a>
		</div>
	</div>
</div>

<style>

		a {
				text-decoration: none;
				color: white;
		}


		.nav-title-sub {
				display: none;
				transition: 0.5s ease;
				color: white;
		}

		.nav-title {
				font-size: 35px;
				text-align: center;
				margin: 3% 0 0 0;
        transition: 0.5s ease;
				color: white;
		}

		.container-side-nav-bar:hover .nav-title {
				display: none;
		}

    .container-side-nav-bar:hover .nav-title-sub {
				display: unset;
        text-align: center;
        margin: 7% 0 0 0 ;
    }

		.container-side-nav-bar {
				display: flex;
				flex-direction: column;
				height: 100vh;
				width: 10%;
				margin: 0;
        background-color: #1F2937;
				transition: 0.5s ease;
				border-radius: 3px;
		}


    .container-side-nav-bar:hover {
        width: 15%;
    }

		.side-nav-bar {
				display: flex;
				flex-direction: column;
				margin: 10% 3% 0 5%;
		}

		.item-nav-container {
				margin: 5% 0 0 0;
				border-radius: 3px;
				padding: 5%;
				text-align: center;
		}

		.item-nav-container:hover {
        background-color: #303e56;
				transform: scale(1.15);
		}

		.item-icon {
				font-size: 35px;
				align-self: center;
				color: white;
				transition: 0.5s ease;
				margin: 10% 0 0 0;
		}


		.item-nav-desc {
				display: none;
		}

		.container-side-nav-bar:hover .item-nav-desc {
				display: inline;
				font-size: 20px;
				margin: auto auto auto 15%;
		}

		.container-side-nav-bar:hover .item-icon {
				margin: auto;
		}

		.container-side-nav-bar:hover .item-nav-container {
				text-align: unset;
        box-shadow: 0 10px 20px rgb(0,0,0, .2);
		}

</style>
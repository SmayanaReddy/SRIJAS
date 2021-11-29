from importlib.machinery import SourceFileLoader
goinglobal_scraper = SourceFileLoader('goinglobal_scrapper', 'code/Scraper/goinglobal_scrapper.py').load_module()

def test_get_job_goin_global(mocker):
    final_result = goinglobal_scraper.get_jobs("Programmer", "", 5, ["Programmer", "Analytic", "Experience"])
    assert final_result is not None
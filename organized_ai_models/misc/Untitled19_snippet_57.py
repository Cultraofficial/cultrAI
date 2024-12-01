def check_all_pipelines():
    print("Checking all pipelines...")
    pipelines = aiplatform.PipelineJob.list()
    if not pipelines:
        print("No active pipelines found.")
    else:
        for pipeline in pipelines:
            print(f"Pipeline: {pipeline.display_name}, State: {pipeline.state}")

check_all_pipelines()

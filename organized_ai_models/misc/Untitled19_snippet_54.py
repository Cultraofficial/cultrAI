def check_pipelines():
    print("Checking active pipelines...")
    pipelines = aiplatform.PipelineJob.list()
    if not pipelines:
        print("No active pipelines found.")
    else:
        for pipeline in pipelines:
            print(f"Pipeline: {pipeline.display_name}, State: {pipeline.state}")
check_pipelines()

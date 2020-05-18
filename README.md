# Large-Scale Computing for the Social Sciences
### Spring 2020 - MACS 30123/MAPS 30123/PLSC 30123

| Instructor Information | **TA Information** | Course Information     |
| :-------------         | :-------------     | :------------          |
| Jon Clindaniel         | Dhruval Bhatt      | Location: [Online](https://canvas.uchicago.edu/courses/28258)   |
| 1155 E. 60th Street, Rm. 215 |              | Monday/Wednesday       |
| jclindaniel@uchicago.edu | dhruval@uchicago.edu | 9:30-11:20 AM (CDT)|
| **Office Hours:** [Schedule](https://appoint.ly/s/jclindaniel/office-hours)\* | **Office Hours:** [Schedule](https://appoint.ly/s/dhruval/office_hours)\*| **Lab:** Prerecorded, [Online](https://canvas.uchicago.edu/courses/28258)|

\* Office Hours held via Zoom

## Course Description
Computational social scientists increasingly need to grapple with data that is either too big for a local machine and/or code that is too resource intensive to process on a local machine. In this course, students will learn how to effectively scale their computational methods beyond their local machines. The focus of the course will be social scientific applications, ranging from training machine learning models on large economic time series to processing and analyzing social media data in real-time. Students will be introduced to several large-scale computing frameworks such as MPI, MapReduce, Spark, and OpenCL, with a special emphasis on employing these frameworks using cloud resources and the Python programming language.

*Prerequisites: CAPP 30121 and CAPP 30122, or equivalent.*

## Course Structure
This course is structured into several modules, or overarching thematic learning units, focused on teaching students fundamental large-scale computing concepts, as well as giving them the opportunity to apply these concepts to Computational Social Science research problems. Students can access the content in these modules on the [Canvas course site](https://canvas.uchicago.edu/courses/28258). Each module consists of a series of asynchronous lectures, readings, and assignments, which will make up a portion of the instruction time each week. If students have any questions about the asynchronous content, they should post these questions in the Piazza forum for the course, which they can access by clicking the "Piazza" tab on the left side of the screen on the Canvas course site. To see an overall schedule and syllabus for the course, as well as access additional course-related files, please visit the GitHub Course Repository, available here.

Additionally, students will attend short, interactive Zoom sessions during regular class hours (starting at 9:30 AM CDT) on Mondays and Wednesdays meant to give them the opportunity to discuss and apply the skills they have learned asynchronously and receive live instructor feedback. Attendance to the synchronous class sessions is mandatory and is an important component of the final course grade. Students can access the Zoom sessions by clicking on the "Zoom" tab on the left side of the screen on the Canvas course site. Students should prepare for these classes by reading the assigned readings ahead of every session. All readings are available online and are linked in the course schedule below.

Students will also virtually participate in a hands-on Python lab section each week, meant to instill practical large-scale computing skills related to the week’s topic. These labs are accessible on the Canvas course site and related code will be posted here in this GitHub repository. In order to practice these large-scale computing skills and complete the course assignments, students will be given free access to UChicago's [Midway Research Computing Cluster](https://rcc.uchicago.edu/docs/), [Amazon Web Services (AWS)](https://aws.amazon.com/) cloud computing resources, and [DataCamp](https://www.datacamp.com/). More information about accessing these resources will be provided to registered students in the first several weeks of the quarter.

## Grading
There will be an assignment due at the end of each unit (3 in total). Each assignment is worth 20% of the overall grade, with all assignments together worth a total of 60%. Additionally, attendance and participation will be worth 10% of the overall grade. Finally, students will complete a final project that is worth 30% of the overall grade (25% for the project itself, and 5% for an end-of-quarter presentation).

| Course Component         | Grade Percentage  |
| :-------------           | :-------------    |
| Assignments (Total: 3)   | 60%               |
| Attendance/Participation | 10%               |
| Final Project            | 5% (Presentation) |
|                          | 25% (Project)     |

Students do have the option of taking this course on a pass/fail basis. Note that in order to earn a "Pass," students must earn at least a B- (80%) in each of the above course components (including participation) and inform the instructor that they would like to be graded on a pass/fail basis before their Final Project due date.

## Final Project
For their final project (due 6/11/2020\*), students will write their own large-scale computing code that solves a social science research problem of their choosing. For instance, students might perform a computationally intensive demographic simulation, collect and analyze large-scale streaming social media data, or train a machine learning model on a large-scale economic dataset. Students will additionally record a short video presentation about their project in the final week of the course. Detailed descriptions and grading rubrics for the project and presentation are available [on the Canvas course site.](https://canvas.uchicago.edu/courses/28258)

\* Due 6/5/2020 for students graduating in June

## Late Assignments/Projects
Unexcused Late Assignment/Project Submissions will be penalized 10 percentage points for every hour they are late. For example, if an assignment is due on Wednesday at 2:00pm, the following percentage points will be deducted based on the time stamp of the last commit.

| Example last commit |	Percentage points deducted         |
| ----                | ----                               |
| 2:01pm to 3:00pm    |	-10 percentage points              |
| 3:01pm to 4:00pm    |-20 percentage points               |
| 4:01pm to 5:00pm    | -30 percentage points              |
| 5:01pm to 6:00pm    | -40 percentage points              |
| ...                 |	...                                |
| 11:01pm and beyond  |	-100 percentage points (no credit) |

## Plagiarism on Assignments/Projects
Academic honesty is an extremely important principle in academia and at the University of Chicago.
* Writing assignments must quote and cite any excerpts taken from another work.
* If the cited work is the particular paper referenced in the Assignment, no works cited or references are necessary at the end of the composition.
* If the cited work is not the particular paper referenced in the Assignment, you MUST include a works cited or references section at the end of the composition.
* Any copying of other students' work will result in a zero grade and potential further academic discipline.
If you have any questions about citations and references, consult with your instructor.

## Statement of Diversity and Inclusion
The University of Chicago is committed to diversity and rigorous inquiry from multiple perspectives. The MAPSS, CIR, and Computation programs share this commitment and seek to foster productive learning environments based upon inclusion, open communication, and mutual respect for a diverse range of identities, experiences, and positions.

Any suggestions for how we might further such objectives both in and outside the classroom are appreciated and will be given serious consideration. Please share your suggestions or concerns with your instructor, your preceptor, or your program’s Diversity and Inclusion representatives: Darcy Heuring (MAPSS), Matthias Staisch (CIR), and Chad Cyrenne (Computation). You are also welcome and encouraged to contact the Faculty Director of your program.

This course is open to all students who meet the academic requirements for participation. Any student who has a documented need for accommodation should contact Student Disability Services (773-702-6000 or disabilities@uchicago.edu) and the instructor as soon as possible.

## Course Schedule
| Unit   | Week | Day | Topic | Readings | Assignment |
| --- | --- | --- | --- | --- |  --- |
| Fundamentals of Large-Scale Computing | Week 1: Introduction to Large-Scale Computing for the Social Sciences | 4/6/2020 | Introduction to the course and course goals | | |
| | | 4/8/2020 | General Considerations for Large-Scale Computing | [Robey and Zamora 2020 (Chapter 1)](https://livebook.manning.com/book/parallel-and-high-performance-computing/chapter-1) | |
| | Week 2: On-Premise Large-Scale CPU-computing with MPI | 4/13/2020 | An Introduction to CPUs and Research Computing Clusters | [Pacheco 2011](https://canvas.uchicago.edu/files/3391260/download?download_frd=1) (Ch. 1-2), [Midway RCC User Guide](https://rcc.uchicago.edu/docs/) | |
| | | 4/15/2020 | Cluster Computing via Message Passing Interface (MPI) for Python | [Pacheco 2011](https://canvas.uchicago.edu/files/3391260/download?download_frd=1) (Ch. 3), [Dalcín et al. 2008](https://www-sciencedirect-com.proxy.uchicago.edu/science/article/pii/S0743731507001712?via%3Dihub) | |
|||| Lab: Hands-on Introduction to UChicago's Midway Computing Cluster and mpi4py |||
| | Week 3: On-Premise GPU-computing with OpenCL | 4/20/2020 | An Introduction to GPUs and Heterogenous Computing with OpenCL | [Scarpino 2012](https://canvas.uchicago.edu/files/3391262/download?download_frd=1) (Read Ch. 1, Skim Ch. 2-5,9) | |
| | | 4/22/2020 | Harnessing GPUs with PyOpenCL | [Klöckner et al. 2012](https://arxiv.org/pdf/0911.3456.pdf) | |
|||| Lab: Introduction to PyOpenCL and GPU Computing on UChicago's Midway Computing Cluster |||
| Architecting Computational Social Science Data Solutions in the Cloud | Week 4: An Introduction to Cloud Computing and Cloud HPC Architectures | 4/27/2020 | An Introduction to the Cloud Computing Landscape and AWS | [Jorissen and Bouffler 2017](https://canvas.uchicago.edu/files/3391263/download?download_frd=1) (Read Ch. 1, Skim Ch. 4-7), [Armbrust et al. 2009](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2009/EECS-2009-28.pdf), [Jonas et al. 2019](https://arxiv.org/pdf/1902.03383.pdf) | |
| | | 4/29/2020 | Architectures for Large-Scale Computation in the Cloud | [Introduction to HPC on AWS](https://d1.awsstatic.com/whitepapers/Intro_to_HPC_on_AWS.pdf), [HPC Architectural Best Practices](https://d1.awsstatic.com/whitepapers/architecture/AWS-HPC-Lens.pdf) | Due: Assignment 1 (11:59 PM) |
|||| Lab: Running "Serverless" HPC Jobs in the AWS Cloud |||
| | Week 5: Architecting Large-Scale Data Solutions in the Cloud | 5/4/2020 | "Data Lake" Architectures | [Data Lakes and Analytics on AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/), [AWS Data Lake Whitepaper](https://d1.awsstatic.com/whitepapers/Storage/data-lake-on-aws.pdf), [*Introduction to AWS Boto in Python*](https://campus.datacamp.com/courses/introduction-to-aws-boto-in-python) (DataCamp Course; Practice working with S3 Data Lake in Python) | |
| | | 5/6/2020 | Architectures for Large-Scale Data Structuring and Storage | General, Open Source: ["What is a Database?" (YouTube),](https://www.youtube.com/watch?v=Tk1t3WKK-ZY) ["How to Choose the Right Database?" (YouTube),](https://www.youtube.com/watch?v=v5e_PasMdXc)  [“NoSQL Explained,”](https://www.mongodb.com/nosql-explained) AWS-specific solutions: ["Which Database to Use When?" (YouTube),](https://youtu.be/KWOSGVtHWqA) Optional: [Data Warehousing on AWS Whitepaper](https://d0.awsstatic.com/whitepapers/enterprise-data-warehousing-on-aws.pdf), [AWS Big Data Whitepaper](https://d1.awsstatic.com/whitepapers/Big_Data_Analytics_Options_on_AWS.pdf) | |
|||| Lab: Exploring Large Data Sources in an S3 Data Lake with the AWS Python SDK, Boto |||
| | Week 6: Large-Scale Data Ingestion and Processing | 5/11/2020 | Stream Ingestion and Processing with Apache Kafka, AWS Kinesis | [Narkhede et al. 2017](https://canvas.uchicago.edu/files/3391266/download?download_frd=1) (Read Ch. 1, Skim 3-6,11), [Dean and Crettaz 2019 (Ch. 4)](https://livebook.manning.com/book/event-streams-in-action/chapter-4/), [AWS Kinesis Whitepaper](https://d0.awsstatic.com/whitepapers/whitepaper-streaming-data-solutions-on-aws-with-amazon-kinesis.pdf) ||
| | | 5/13/2020 | Batch Processing with Apache Hadoop and MapReduce | [White 2015](https://canvas.uchicago.edu/files/3391265/download?download_frd=1) (read Ch. 1-2, Skim 3-4), [Dean and Ghemawat 2004](https://www.usenix.org/legacy/publications/library/proceedings/osdi04/tech/full_papers/dean/dean.pdf), ["What is Amazon EMR?"](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html), Running MapReduce Jobs with Python’s “mrjob” package on EMR ([Fundamentals](https://mrjob.readthedocs.io/en/latest/guides/quickstart.html) and [Elastic MapReduce Quickstart](https://mrjob.readthedocs.io/en/latest/guides/emr-quickstart.html)) | |
|||| Lab: Ingesting and Processing Batch Data with MapReduce on AWS EMR and Streaming Data with AWS Kinesis | ||
| Large-Scale Data Analysis and Prediction | Week 7: An Introduction to High-Level Large-Scale Computing Paradigms for Data Analysis and Prediction | 5/18/2020 | Large-Scale Data Processing and Analysis with Spark and Dask | [Karau et al. 2015](https://canvas.uchicago.edu/files/3391268/download?download_frd=1) (Read Ch. 1-4, Skim 9-11), [*Introduction to PySpark*](https://learn.datacamp.com/courses/introduction-to-pyspark) (DataCamp Course), [“Why Dask,”](https://docs.dask.org/en/latest/why.html) [Dask Slide Deck](https://dask.org/slides.html),  Optional: [*Parallel Programming with Dask*](https://learn.datacamp.com/courses/parallel-programming-with-dask-in-python) (DataCamp Course) | |
| | | 5/20/2020 | A Deeper Dive into Spark (with Social Science Machine Learning Applications) | [*Machine Learning with PySpark*](https://campus.datacamp.com/courses/machine-learning-with-pyspark) (DataCamp Course), Optional: [*Feature Engineering with PySpark*](https://learn.datacamp.com/courses/feature-engineering-with-pyspark) (DataCamp Course), Videos about accelerating Spark with GPUs (via [Horovod](https://www.youtube.com/watch?v=D1By2hy4Ecw) for deep learning, and the RAPIDS Library for general operations [Part 1](https://www.youtube.com/watch?v=Qw-TB6EHmR8) and [Part 2](https://www.youtube.com/watch?v=ApI2EZIJU_Q)) | Due: Assignment 2 (11:59 PM) |
|||| Lab: Running PySpark in an AWS EMR Notebook for Large-Scale Data Analysis and Prediction |||
| | Week 8: Large-Scale Network Analysis | 5/25/2020 | Memorial Day (No Class) | | |
| | | 5/27/2020 | Processing and Analyzing Large-Scale Graphs with Spark | [Guller 2015](https://canvas.uchicago.edu/files/3391270/download?download_frd=1), [Hunter 2017](https://www.youtube.com/watch?v=NmbKst7ny5Q) (Spark Summit Talk), [GraphFrames Documentation for Python](https://docs.databricks.com/spark/latest/graph-analysis/graphframes/user-guide-python.html) | |
|||| Lab: Network Analysis with PySpark |||
| Student Projects and Presentations | Week 9: Final Project Presentations | 6/1/2020 | View and Comment on Student Presentations |  | Due: Final Project Presentation Video (9:30 AM) |
||| 6/3/2020 | View and Comment on Student Presentations |  | Due: Assignment 3 (11:59 PM) |
||| 6/5/2020 ||| Due: Final Project (11:59 PM; For June 2020 Graduates)
|| Week 10: Final Projects | 6/11/2020 ||| Due: Final Project (11:59 PM; For all other students) |

## Works Cited

Armbrust, Michael, Fox, Armando, Griffith, Rean, Joseph, Anthony D., Katz, Randy H., Konwinski, Andrew, Lee, Gunho, Patterson, David A., Rabkin, Ariel, Stoica, Ion, and Matei Zaharia. 2009. "Above the Clouds: A Berkeley View of Cloud Computing." Technical report, EECS Department, University of California, Berkeley.

["AWS Big Data Analytics Options on AWS." December 2018.)](https://d1.awsstatic.com/whitepapers/Big_Data_Analytics_Options_on_AWS.pdf) AWS Whitepaper.

["Building Big Data Storage Solutions (Data Lakes) for Maximum Flexibility." July 2017.](https://d1.awsstatic.com/whitepapers/Storage/data-lake-on-aws.pdf)

Dalcín, Lisandro, Paz, Rodrigo, Storti, Mario, and Jorge D'Elía. 2008. "MPI for Python: Performance improvements and MPI-2 extensions." *J. Parallel Distrib. Comput.* 68: 655-662.

["Data Warehousing on AWS." March 2016.](https://d0.awsstatic.com/whitepapers/enterprise-data-warehousing-on-aws.pdf) AWS Whitepaper.

Dean, Alexander, and Valentin Crettaz. 2019. *Event Streams in Action: Real-time event systems with Kafka and Kinesis*. Shelter Island, NY: Manning.

Dean, Jeffrey, and Sanjay Ghemawat. 2004. "MapReduce: Simplified data processing on large clusters." In *Proceedings of Operating Systems Design and Implementation (OSDI)*. San Francisco, CA. 137-150.

*Feature Engineering with PySpark*. https://learn.datacamp.com/courses/feature-engineering-with-pyspark. Accessed 3/2020.

"GraphFrames user guide - Python." https://docs.databricks.com/spark/latest/graph-analysis/graphframes/user-guide-python.html. Accessed 3/2020.

Guller, Mohammed. 2015. "Graph Processing with Spark." In *Big Data Analytics with Spark*. New York: Apress.

["High Performance Computing Lens AWS Well-Architected Framework." December 2019.](https://d1.awsstatic.com/whitepapers/architecture/AWS-HPC-Lens.pdf) AWS Whitepaper.

Hunter, Tim. October 26, 2017. "GraphFrames: Scaling Web-Scale Graph Analytics with Apache Spark." https://www.youtube.com/watch?v=NmbKst7ny5Q.

*Introduction to AWS Boto in Python*. https://campus.datacamp.com/courses/introduction-to-aws-boto-in-python. Accessed 3/2020.

["Introduction to HPC on AWS." n.d.](https://d1.awsstatic.com/whitepapers/Intro_to_HPC_on_AWS.pdf) AWS Whitepaper.

*Introduction to PySpark*. https://learn.datacamp.com/courses/introduction-to-pyspark. Accessed 3/2020.

Jonas, Eric, Schleier-Smith, Johann, Sreekanti, Vikram, and Chia-Che Tsai. 2019. "Cloud Programming Simplified: A Berkeley View on Serverless Computing." Technical report, EECS Department, University of California, Berkeley.

Jorissen, Kevin, and Brendan Bouffler. 2017. *AWS Research Cloud Program: Researcher's Handbook*. Amazon Web Services.

Kane, Frank. March 23, 2018. ["How to Choose the Right Database? - MongoDB, Cassandra, MySQL, HBase"](https://www.youtube.com/watch?v=v5e_PasMdXc). https://www.youtube.com/watch?v=v5e_PasMdXc

Karau, Holden, Konwinski, Andy, Wendell, Patrick, and Matei Zaharia. 2015. *Learning Spark*. Sebastopol, CA: O'Reilly.

Klöckner, Andreas, Pinto, Nicolas, Lee, Yunsup, Catanzaro, Bryan, Ivanov, Paul, and Ahmed Fasih. 2012. "PyCUDA and PyOpenCL: A Scripting-Based Approach to GPU Run-Time Code Generation." *Parallel Computing* 38(3): 157-174.

Linux Academy. July 10, 2019. ["What is a Database?"](https://www.youtube.com/watch?v=Tk1t3WKK-ZY). https://www.youtube.com/watch?v=Tk1t3WKK-ZY

*Machine Learning with PySpark*. https://campus.datacamp.com/courses/machine-learning-with-pyspark. Accessed 3/2020.

Martinez, Miguel, and Thomas Graves. "Accelerating Apache Spark by Several Orders of Magnitude with GPUs." https://www.youtube.com/watch?v=Qw-TB6EHmR8.

"mrjob v0.7.1 documentation." https://mrjob.readthedocs.io/en/latest/index.html. Accessed 3/2020.

Narkhede, Neha, Shapira, Gwen, and Todd Palino. 2017. *Kafka: The Definitive Guide*. Sebastopol, CA: O'Reilly.

“NoSQL Explained.” https://www.mongodb.com/nosql-explained. Accessed 3/2020.

Pacheco, Peter. 2011. *An Introduction to Parallel Programming*. Burlington, MA: Morgan Kaufmann.

*Parallel Programming with Dask*. https://learn.datacamp.com/courses/parallel-programming-with-dask-in-python. Accessed 3/2020.

Petrossian, Tony, and Ian Meyers. November 30, 2017. "Which Database to Use When?" https://youtu.be/KWOSGVtHWqA. AWS re:Invent 2017.

"RCC User Guide." rcc.uchicago.edu/docs/. Accessed March 2020.

Robey, Robert and Yuliana Zamora. 2020. *Parallel and High Performance Computing*. Manning Early Access Program.

Scarpino, Matthew. 2012. *OpenCL in Action*. Shelter Island, NY: Manning.

Sergeev, Alex. March 28, 2019. "Distributed Deep Learning with Horovod." https://www.youtube.com/watch?v=D1By2hy4Ecw.

["Streaming Data Solutions on AWS with Amazon Kinesis." July 2017.](https://d0.awsstatic.com/whitepapers/whitepaper-streaming-data-solutions-on-aws-with-amazon-kinesis.pdf) AWS Whitepaper.

"What is Amazon EMR." https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html. Accessed 3/2020.

White, Tom. 2015. *Hadoop: The Definitive Guide*. Sebastopol, CA: O'Reilly.

"Why Dask." https://docs.dask.org/en/latest/why.html. Accessed 3/2020.

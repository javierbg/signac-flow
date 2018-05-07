import flow
from flow import FlowProject


class TestProject(FlowProject):
    pass


@TestProject.label
def default_label(job):
    return True


@TestProject.label
def negative_default_label(job):
    return False


@TestProject.label
def b_is_even(job):
    return job.sp.b % 2 == 0


@TestProject.operation
@flow.cmd
@TestProject.pre(b_is_even)
@TestProject.post.isfile('world.txt')
def op1(job):
    return 'echo "hello" > {job.ws}/world.txt'


@TestProject.operation
def op2(job):
    job.document.test = True


if __name__ == '__main__':
    TestProject().main()
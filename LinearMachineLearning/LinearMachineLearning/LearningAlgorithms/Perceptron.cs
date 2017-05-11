using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using LinearMachineLearning.DataHandling;

namespace LinearMachineLearning.LearningAlgorithms
{
    public class Perceptron : LinearModel
    {
        #region Parameters
        public double[] Pocket { get; set; }
        public double PreviousInSampleError { get; set; }
        #endregion

        #region Constructors
        public Perceptron()
        {
            InputSize = 1;
            Inputs = new double[InputSize];
            Weights = new double[InputSize];
            Pocket = new double[InputSize];
            Output = 0;
            InSampleError = 0;
            PreviousInSampleError = 0;
        }
        public Perceptron(int inputSize)
        {
            InputSize = inputSize;
            Inputs = new double[InputSize];
            Weights = new double[InputSize];
            Pocket = new double[InputSize];
            Output = 0;
            InSampleError = 0;
            PreviousInSampleError = 0;
        }
        public Perceptron(string filePath)
        {
            FilePath = filePath;
            string[] lines = System.IO.File.ReadAllLines(filePath);

            Name = lines[0];
            InputSize = Convert.ToInt32(lines[1]);
            Inputs = new double[InputSize];
            Weights = new double[InputSize];
            Pocket = new double[InputSize];

            string[] stringWeights = lines[2].Split(',');
            for (int index = 0; index < stringWeights.Length; index++)
            {
                Weights[index] = Convert.ToDouble(stringWeights[index]);
                Pocket[index] = Weights[index];
            }

            InSampleError = 0;
            PreviousInSampleError = 0;
            Output = 0;
        }
        #endregion

        #region Methods
        public override void ComputeOutput(double[] input)
        {
            base.ComputeOutput(input);
            Output = Math.Sign(Output);
        }
        public override void Train(DataPoint point)
        {
            base.Train(point);
        }
        public override void Learn(DataSet set)
        {
            base.Learn(set);
        }
        public override void ComputeInSampleError(DataSet set)
        {
            InSampleError = 0;
            foreach (DataPoint point in set.Examples)
            {
                if(ComputeSinglePointError(point) != 0)
                {
                    InSampleError++;
                }
            }
            InSampleError /= set.NumberExamples;
        }
        public override double ComputeSinglePointError(DataPoint point)
        {
            ComputeOutput(point.Input);
            return Output - point.Output;
        }
        #endregion
    }
}
